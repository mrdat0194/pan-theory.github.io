import sys
import copy
from typing import List, Optional
from dataclasses import dataclass


class Tiles:
    safe: List[List[bool]]

    @staticmethod
    def parse(lines: List[str]) -> 'Tiles':
        t = Tiles()
        t.safe = []
        for line in lines:
            t.safe.append([c == '.' for c in line])
        return t


@dataclass
class State:
    bikes: List[List[int]]
    speed: int
    prev_actions: List[str]

    def can_use(self, action: str) -> bool:
        if action == 'SPEED':
            return True
        elif action == 'SLOW':
            return self.speed > 1
        elif action == 'JUMP':
            return True
        elif action == 'WAIT':
            return True
        elif action == 'UP':
            return min(b[1] for b in self.bikes) > 0
        elif action == 'DOWN':
            return max(b[1] for b in self.bikes) < 3
        else:
            raise ValueError

    def exec_action(self, action: str, tiles: Tiles) -> 'State':
        assert self.can_use(action)
        s = copy.deepcopy(self)
        y_delta = 0
        # exec action
        if action == 'SPEED':
            s.speed += 1
        elif action == 'SLOW':
            s.speed -= 1
        elif action == 'UP':
            y_delta = -1
        elif action == 'DOWN':
            y_delta = 1

        # move
        move_delta = (s.speed, y_delta)
        for i in reversed(range(len(s.bikes))):
            if State._check_destroyed(s.bikes[i], move_delta, tiles, action == 'JUMP'):
                del s.bikes[i]
            else:
                s.bikes[i][0] += move_delta[0]
                s.bikes[i][1] += move_delta[1]

        s.prev_actions.append(action)
        return s

    @staticmethod
    def _check_destroyed(bike, delta, tiles: Tiles, is_jump: bool) -> bool:
        if is_jump:
            return bike[0] + delta[0] < len(tiles.safe[0]) and not tiles.safe[bike[1] + delta[1]][bike[0] + delta[0]]

        for y in [bike[1], bike[1] + delta[1]]:
            for x in range(bike[0] + 1, bike[0] + delta[0] + (1 if y == bike[1] + delta[1] else 0)):
                if x < len(tiles.safe[0]) and not tiles.safe[y][x]:
                    return True
        return False


class Algorithm:
    def __init__(self, tiles: Tiles, min_bikes: int):
        self.tiles = tiles
        self.min_bikes = min_bikes

    def step(self, state: State) -> Optional[List[str]]:
        if len(state.bikes) < self.min_bikes:
            return None
        if self._is_done(state):
            return state.prev_actions + ['WAIT']

        for action in ['SPEED', 'SLOW', 'JUMP', 'WAIT', 'UP', 'DOWN']:
            print(f'checking {action}, path len: {len(state.prev_actions)}', file=sys.stderr)
            if not state.can_use(action):
                continue
            res = self.step(state.exec_action(action, self.tiles))
            if res:
                return res
        return None

    def _is_done(self, state: State) -> bool:
        return state.bikes[0][0] >= len(self.tiles.safe[0]) - 1


####
# sys.stdin = open('input.txt', 'r')
####

m = int(input())  # the amount of motorbikes to control
v = int(input())  # the minimum amount of motorbikes that must survive
tiles = Tiles.parse([input() for _ in range(4)])
init_speed = int(input())
bikes = [[int(i) for i in input().split()][:2] for _ in range(m)]

state = State(bikes, init_speed, [])
print(f'initial state: {state}', file=sys.stderr)
path = Algorithm(tiles, v).step(state)
print(f'found path: {path}', file=sys.stderr)
# assert path

for c in path:
    print(c)

    if sys.stdin == sys.__stdin__:
        # discard state
        for _ in range(m + 1):
            input()
