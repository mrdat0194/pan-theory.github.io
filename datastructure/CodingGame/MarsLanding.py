'''
6         	(surfaceN) Surface made of 6 points
0 1500      	(landX landY)
1000 2000	(landX landY)
2000 500	(landX landY) Start of flat ground
3500 500	(landX landY) End of flat ground
5000 1500	(landX landY)
6999 1000	(landX landY)

5000 2500 -50 0 1000 90 0 (X Y hSpeed vSpeed fuel rotate power)
'''
import numpy as np
import sys
from time import time

# Parameters of the genetic algorithm
ELITISM = 0.20
GENERATIONS = 40
MUTATION = 0.05
NUMBER = 40
LENGTH = 200
G = -3.711

# Read the surface line
surfaceN = int(input())
surfaceX, surfaceY = [], []
for _ in range(surfaceN):
    x, y = map(int, input().split())
    surfaceX.append(x)
    surfaceY.append(y)
surfaceX = np.array(surfaceX)
surfaceY = np.array(surfaceY)

# Find the landing zone and compute curvilign distances
surface_lengths = []
for i in range(surfaceN - 1):
    surface_lengths.append(
        np.sqrt(
            (surfaceY[i + 1] - surfaceY[i]) ** 2
            + (surfaceX[i + 1] - surfaceX[i]) ** 2
        )
    )
    if surfaceY[i + 1] == surfaceY[i]:
        land_segment = i
        landX = (surfaceX[i + 1] + surfaceX[i]) / 2
        min_dist = (surfaceX[i + 1] - surfaceX[i]) / 2
        landY = surfaceY[i]

# Geometry
def is_intersecting(ax, ay, bx, by, cx, cy, dx, dy):
    denominator = ((bx - ax) * (dy - cy)) - ((by - ay) * (dx - cx))
    numerator1 = ((ay - cy) * (dx - cx)) - ((ax - cx) * (dy - cy))
    numerator2 = ((ay - cy) * (bx - ax)) - ((ax - cx) * (by - ay))

    return np.where(
        denominator == 0,
        (numerator1 == 0) & (numerator2 == 0),
        ((numerator1 / denominator >= 0) & (numerator1 / denominator <= 1))
        & ((numerator2 / denominator >= 0) & (numerator2 / denominator <= 1)),
        )


def traj_to_crash(vec_x, vec_y, vec_vx, vec_vy):
    ax, bx = surfaceX[:-1], surfaceX[1:]
    ay, by = surfaceY[:-1], surfaceY[1:]
    cx, dx = (
        vec_x[:-1].reshape(LENGTH - 1, 1),
        vec_x[1:].reshape(LENGTH - 1, 1),
    )
    cy, dy = (
        vec_y[:-1].reshape(LENGTH - 1, 1),
        vec_y[1:].reshape(LENGTH - 1, 1),
    )

    intersect = is_intersecting(ax, ay, bx, by, cx, cy, dx, dy).argmax()

    # There is a crash
    if intersect.any():
        crash_segment = intersect % (surfaceN - 1)
        crashI = intersect // (surfaceN - 1) + 1
        crashX, crashY, crashVX, crashVY = (
            vec_x[crashI],
            vec_y[crashI],
            vec_vx[crashI],
            vec_vy[crashI],
        )
        if crash_segment == land_segment:
            crash_dist = np.sqrt((landX - crashX) ** 2 + (landY - crashY) ** 2)
        elif crash_segment < land_segment:
            crash_dist = (
                    np.sqrt(
                        (crashX - surfaceX[crash_segment + 1]) ** 2
                        + (crashY - surfaceY[crash_segment + 1]) ** 2
                    )
                    + sum(surface_lengths[crash_segment + 1 : land_segment])
                    + min_dist
            )
        else:
            crash_dist = (
                    np.sqrt(
                        (crashX - surfaceX[crash_segment]) ** 2
                        + (crashY - surfaceY[crash_segment]) ** 2
                    )
                    + sum(surface_lengths[land_segment + 1 : crash_segment])
                    + min_dist
            )

    else:
        crashI = 0
        crashX, crashY, crashVX, crashVY, crash_dist = 0, 0, 0, 0, 1e4
    return (crashX, crashY, crashVX, crashVY, crash_dist, crashI)


# Fitness function based on physics
def fitness(chrom):
    traj = chrom_to_traj(chrom)
    crashX, crashY, crashVX, crashVY, crash_dist, crashI = traj_to_crash(*traj)
    used_fuel = sum(chrom[:crashI, 0])

    vec = (
            (2 * crash_dist / min_dist) ** 2
            + (crashVY / 20) ** 2
            + (crashVX / 20) ** 2
            + (chrom[crashI, 1] / 15) ** 2
    )
    score = 1 / vec

    score *= np.where((crashI == 0) | (used_fuel > fuel), 1 / 10, 1)

    return score + np.where(
        (crash_dist < min_dist / 2)
        & (abs(crashVX) < 15)
        & (abs(crashVY) < 30)
        & abs(chrom[crashI, 1]) < 10
        & (crashI != 0)
        & (used_fuel <= fuel),
        fuel - used_fuel,
        0,
        )


# Problem specific functions
def init_chromosoms():
    population = []
    for _ in range(NUMBER):

        power_inc = np.random.randint(-1, 2, size=LENGTH)
        angle_inc = np.random.randint(-15, 16, size=LENGTH)

        norm = power + np.cumsum(power_inc)
        angle = rotate + np.cumsum(angle_inc)

        norm = np.minimum(np.maximum(norm, 0), 4)
        angle = np.minimum(np.maximum(angle, -90), 90)
        chromosom = np.array([*zip(norm, angle)])
        population.append(chromosom)
    population = standardize(np.array(population))

    return population


def standardize(chrom):
    chrom[:, :, 0] = np.minimum(np.maximum(chrom[:, :, 0], 0), 4)
    chrom[:, :, 1] = np.minimum(np.maximum(chrom[:, :, 1], -90), 90)

    return chrom


def chrom_to_traj(chrom):
    norm = chrom[:, 0]
    angle = np.radians(chrom[:, 1])

    ax, ay = -norm * np.sin(angle), norm * np.cos(angle) + G
    vec_vx, vec_vy = vx + np.cumsum(ax), vy + np.cumsum(ay)
    vec_x, vec_y = x + np.cumsum(vec_vx), y + np.cumsum(vec_vy)

    return (vec_x, vec_y, vec_vx, vec_vy)


# Genetic algorithms
def selection(population):
    grades = np.array([fitness(chrom) for chrom in population])
    grades -= min(grades)

    index_sort = grades.argsort()[::-1]
    sorted_pop = np.array([population[c] for c in index_sort])
    sorted_grades = np.cumsum(sorted(grades, reverse=True)) / sum(grades)
    new_index = int(ELITISM * NUMBER)
    parents1, parents2 = pairing(sorted_pop, sorted_grades)
    new_chroms1, new_chroms2 = crossover(parents1, parents2)
    sorted_pop[new_index : (new_index + NUMBER) // 2, :, :] = standardize(
        mutation(new_chroms1)
    )

    sorted_pop[
    (new_index + NUMBER) // 2 : NUMBER
                                - ((NUMBER - int(ELITISM * NUMBER)) % 2),
    :,
    :,
    ] = standardize(mutation(new_chroms2))
    return sorted_pop


def pairing(sorted_pop, sorted_grades):
    index1 = np.searchsorted(
        sorted_grades,
        np.random.random(size=((NUMBER - int(ELITISM * NUMBER)) // 2)),
    )
    index2 = np.searchsorted(
        sorted_grades,
        np.random.random(size=((NUMBER - int(ELITISM * NUMBER)) // 2)),
    )

    index2 += np.where(index1 == index2, 1, 0)
    return sorted_pop[index1, :, :], sorted_pop[index2, :, :]


def crossover(chrom1, chrom2):
    mixing = np.random.random(
        size=((NUMBER - int(ELITISM * NUMBER)) // 2, 1, 1)
    )
    new_chrom1 = np.around(chrom1 * mixing + chrom2 * (1 - mixing)).astype(int)
    new_chrom2 = np.around(chrom2 * mixing + chrom1 * (1 - mixing)).astype(int)
    return (new_chrom1, new_chrom2)


def mutation(chrom):
    mutated = np.random.random(size=LENGTH)

    chrom[:, :, 0] += np.cumsum(
        np.where(mutated < MUTATION, np.random.randint(-1, 2, size=LENGTH), 0)
    )
    chrom[:, :, 1] += np.cumsum(
        np.where(
            mutated < MUTATION, np.random.randint(-15, 16, size=LENGTH), 0
        )
    )
    return chrom


for turn in range(LENGTH):

    t0 = time()

    x, y, vx, vy, fuel, rotate, power = map(int, input().split())

    if turn == 0:
        population = init_chromosoms()

        for _ in range(GENERATIONS):
            population = selection(population)

    else:
        for _ in range(10):
            population = selection(population)

    chrom = sorted(population, key=fitness, reverse=True)[0]
    print(fitness(chrom), file=sys.stderr)

    if abs(y - landY) < 2 * abs(vy):
        print(0, chrom[0, 0])
    else:
        print(chrom[0, 1], chrom[0, 0])

    population = np.delete(population, (0,), axis=1)
    LENGTH -= 1

    print("Time for the turn %s" % (time() - t0), file=sys.stderr)
