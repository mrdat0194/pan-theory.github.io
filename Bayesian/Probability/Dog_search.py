import numpy as np
import pandas as pd
from math import erf,sqrt
import matplotlib.pyplot as plt
from numpy import random
import itertools
from scipy.special import comb, factorial

# from pgmpy.models import BayesianModel
# from pgmpy.factors.discrete import TabularCPD

class coin():
    def __init__(self):
        self.num_toss = 10

    def toss_coins(self):
        xpt = np.random.choice(a=['H', 'T'], size=self.num_toss, p=[0.75, 0.25])
        return xpt

    def compute_reward(self, in_seq):
        reward = []
        for idx in range(1, self.num_toss):
            r = in_seq[idx] == 'T' and in_seq[idx-1] == 'H'
            reward.append(r)
        reward_total = np.sum(reward)
        #print(in_seq, '\n', reward,np.sum(reward) )
        return reward_total

    def test_toss(self):
        '''
        Problem 5. Indicator variables S points possible (graded) Consider a sequence of n 1 independent tosses of a biased coin, at times
        k = 0,1,2,...,n. On each toss, the probability of Heads is p, and the probability of Tails is 1 -p {1,2,..,
        at time for E resulted in Tails and the toss at time - 1 resulted in A reward of one unit is given if the toss at time Heads.
        Otherwise, no reward is given at time Let R be the sum of the rewards collected at times 1, 2,...,?
        :return:
        '''

        num_simu = 25000
        r_vals = []
        for idx in range(num_simu):
            trial = coin.toss_coins()
            reward = coin.compute_reward(trial)
            r_vals.append(reward)

        print('Mean R: {0}'.format(np.mean(r_vals)))
        print('Var R: {0}'.format(np.var(r_vals)))

        #Theory

        n = 10
        p = 0.75
        r_mean = n*p*(1-p)
        r_var = n*p*(1-p) + 2*(n-2)*(p**2)*(1-p)**2 + (n-2)*(n-3)*(p**2)*(1-p)**2 - r_mean**2

        print('theory mean: {}'.format(r_mean))
        print('theory_var: {}'.format(r_var))

    def simu_coin_toss(self):
        """Function to simulate a coin toss
        Returns:
            number of tails until first head
        """
        num_tails = 1
        while True:
            head = np.random.uniform(size=1) > 0.5
            #res.append(head[0])
            if not head: # tails
                num_tails += 1
            else:  # heads
                break
        return num_tails

    def twoCoint(self):
        ''' Problem 6: Tossing a pair of coins
        '''
        pass

    def make_Xk(num_tails):
        """ Make a sequence of num_tails+1 uniform random variables"""
        X_k = np.random.uniform(low=0, high=5, size=num_tails+1)
        return X_k

    def make_X(num_tails):
        """ Make r.v. X which is the sum of num_tails+1 uniform r.vs"""
        X_k = coin.make_Xk(num_tails)
        X = np.sum(X_k)
        return X

    def test_toss2(self):
        '''
        Problem 7: Sum of a random number of r.v.'s
        :return:
        '''
        X_array = []
        for i_sim in range(10000):
            num_tails = coin.simu_coin_toss()

            X_k = coin.make_Xk(num_tails)
            X = np.sum(X_k)
            #     print({"{0}: {1}: {2}".format(num_tails, X_k, X)})
            X_array.append(X)
        #     X_array.append(make_X(num_tails))

        print("Mean of r_X: {0}".format(np.mean(X_array)))
        print("Var of r_X: {0}".format(np.var(X_array)))

    def num_toss_until_HT(self):
        num_toss = 1
        num_first_time = 0
        num_second_time = 0
        prev_res = np.random.choice(['H', 'T'], size=1)
        first_succ = False
        second_succ = False
        while (not first_succ) or (not second_succ):
            cur_res = np.random.choice(['H', 'T'], size=1)
            num_toss += 1
            if cur_res == 'H' and prev_res == 'H':
                if not first_succ and not second_succ:
                    num_first_time = num_toss
                    first_succ = True
                else:
                    num_second_time = num_toss
                    second_succ = True
            prev_res = cur_res

        return num_first_time, num_second_time-num_first_time

    def test_tossHT(self):
        nSims = 10000
        num_first_list = []
        num_second_list = []
        for idx in range(nSims):
            tmp = coin.num_toss_until_HT()
            num_first_list.append(tmp[0])
            num_second_list.append(tmp[1])

        print(np.mean(num_first_list))
        print(np.mean(num_second_list))

    def gen_next_state(cur_state):
        '''Problem 4: A simple Markov chain'''
        if cur_state == 1:
            next_state = np.random.choice([1, 2], p=[0.6, 0.4])
        elif cur_state == 2:
            next_state = np.random.choice([1, 2, 3], p=[0.2, 0.5, 0.3])
        elif cur_state == 3:
            next_state = np.random.choice([2, 3], p=[0.1, 0.9])
        return next_state


    def gen_seq(n_samples = 1000):
        out_seq = []
        cur_state = np.random.choice([1, 2, 3])
        count_dict = {}
        # out_seq.append(first_state)
        for idx in range(1, n_samples):
            # cur_state = out_seq[idx-1]
            next_state = coin.gen_next_state(cur_state)
            #out_seq.append(next_state)
            count_dict[next_state] = count_dict.get(next_state, 0) + 1
            cur_state = next_state
        return count_dict

    # P(X2=2|X0=1)

    def gen_2samples(self):
        cur_state = 1
        count_right = 0
        count_right_S1 = 0

        for idx in range(2):
            next_state = coin.gen_next_state(cur_state)
            cur_state = next_state
        if cur_state == 2:
            return True

    def Test_markov(self):
        nSims = 10000
        count = 0
        for idx in range(nSims):
            if coin.gen_2samples():
                count += 1
        print("{0}/{1}= {2:3.2f}".format(count, nSims, count/nSims))

        # 4346/10000= 0.43
        # 45
        # Analyze the x sequence
        nSims = 10000

        counts = coin.gen_seq(nSims)
        for k, v in counts.items():
            print("{0}: {1:3.2f}".format(k, v/nSims))

    # 1: 0.14
    # 2: 0.23
    # 3: 0.63
    # 73
    # Analyze the y sequence

    def gen_seq_Y(n_samples = 1000):
        out_seq = []
        cur_state = np.random.choice([1, 2, 3])
        count_dict = {}
        for idx in range(1, n_samples):
            next_state = coin.gen_next_state(cur_state)
            y_state = next_state - cur_state
            count_dict[y_state] = count_dict.get(y_state, 0) + 1
            cur_state = next_state
        return count_dict

    def Test_seq(self):
        nSims = 10000
        counts = coin.gen_seq_Y(nSims)
        for k, v in counts.items():
            print("{0}: {1:3.2f}".format(k, v/nSims))

    # 0: 0.78
    # 1: 0.11
    # -1: 0.11
    #     4.5 Given that the nth transition was a transition to the right (Yn=1), find (approximately) the probability that the state at time n−1 was state 1 (i.e., Xn−1=1). Assume that n is large.

    def gen_seq_Y2(n_samples = 1000):
        out_seq = []
        cur_state = np.random.choice([1, 2, 3])
        count_right = 0
        count_right_S1 = 0

        for idx in range(1, n_samples):
            next_state = gen_next_state(cur_state)
            y_state = next_state - cur_state
            if y_state == 1:
                count_right += 1
                if cur_state==1:
                    count_right_S1 += 1
            cur_state = next_state
        return count_right, count_right_S1

    def test_seq2(self):
        nSims = 10000
        counts, counts_S1 = coin.gen_seq_Y2(nSims)
        print("{0}/{1}= {2:3.2f}".format(counts_S1, counts, counts_S1/counts))
# 441/1103= 0.40
# Suppose that X0=1. Let T be the first positive time index n at which the state is equal to 1.

    def time_to_S1():
        cur_state = 1
        count_val = 0
        succ = False
        while not succ:
            next_state = coin.gen_next_state(cur_state)
            count_val += 1
            if next_state == 1:
                succ = True
            cur_state = next_state
        return count_val

    def test_time_s1(self):
        count_list = []
        nSims = 5000
        for idx in range(nSims):
            count_list.append(coin.time_to_S1())
        print(np.mean(count_list))

class Coupon_collector():
    def num_repeats(self):
        num_tosses = 0
        options = ['a', 'b', 'c', 'd', 'e', 'f']
        while options:
            c = np.random.choice(['a', 'b', 'c', 'd', 'e', 'f'], size=1)
            num_tosses += 1
            if c in options:
                options.remove(c)
        return num_tosses

    def Coupon(self):
        res = []
        n_simu = 50000
        for i in range(n_simu):
            res.append(Coupon_collector.num_repeats())
        print(np.mean(np.array(res)))



class Hat():
    def Hat_back_everyone(self):
        num_people = 6
        people_list = list(range(0, num_people))

        num_simu = 10000
        count = 0
        for idx in range(num_simu):
            tmp = np.random.choice(people_list, size=num_people, replace=False)
            if list(tmp) == people_list:
                count += 1
        print(count/num_simu)
        #theory
        # print(1/factorial(num_people))
    def Hat_back_each(self):
        # Each one of persons 1,…,m gets his or her own hat back, where 1≤m≤n.
        num_people = 6
        m = 3
        people_list = list(range(0, num_people))

        num_simu = 10000
        count = 0
        for idx in range(num_simu):
            tmp = np.random.choice(people_list, size=num_people, replace=False)
            if list(tmp[0:m]) == people_list[0:m]:
                count += 1
        print(count/num_simu)
        # n = num_people
        # print(factorial(n-m)/factorial(n))

class Card_dealt():
    def cardDealt(self):
        SUITS = 'cdhs'
        RANKS = '23456789TJQKA'
        DECK = tuple(''.join(card) for card in itertools.product(RANKS, SUITS))
        # What is the probability the 13th card dealt is a King?
        N = 50000
        sum = 0
        for idx in range(N):
            hand = random.sample(DECK, 13)
            if 'K' in hand[-1]:
                sum += 1
        sum/N

        # Theory
        num = np.arange(start=51, stop=51-12, step=-1)
        den = np.arange(start=52, stop=52-13, step=-1)
        # ?np.arange
        # print(num,den)
        # print(4 * np.exp(np.sum(np.log(num)) - np.sum(np.log(den))))
        ans = 4/52
        print(ans)

        # First King dealt
        N = 50000
        sum = 0
        for idx in range(N):
            hand = random.sample(DECK, 13)
            hand = [x[0] for x in hand]
            last_K = 'K' in hand[-1]
            only_K = 'K' not in hand[0:-1]
            if last_K and only_K:
                sum += 1
        sum/N

        # 4/13 * comb(48, 12)/comb(52, 13)

class DivideClass:
    def mk_three_groups(num_students=9):
        """simulate making three groups of students"""
        my_class = list(range(0, num_students))
        num_per_class = num_students//3

        gp1 = random.sample(my_class, num_per_class)
        rem_class = [x for x in my_class if x not in gp1]

        gp2 = random.sample(rem_class, num_per_class)
        gp3 = [x for x in rem_class if x not in gp2]

        return gp1, gp2, gp3

    def in_same_class(groups):
        """ Check if two students are in the same class"""
        succ = False
        for gp in groups:
            succ = (0 in gp) and (1 in gp)
            if succ:
                break
        return succ
    def test(self):
        num_sim = 10000
        num_succ = 0
        for i_sum in range(num_sim):
            groups = DivideClass.mk_three_groups(num_students=90)
            if DivideClass.in_same_class(groups):
                num_succ += 1
        print(num_succ/num_sim)

class Umbrella:
    def Rain(self):
        N = 100000
        prob_forecast = 0.2
        prob_seen = 0.8


        forecast = np.random.rand(N) <= prob_forecast
        seen = np.random.rand(N) <= prob_seen
        umbrella = np.array([False]*N)
        rain = np.array([False]*N)

        # decision on rain
        for idx, f in enumerate(forecast):
            if f:
                r = np.random.rand(1) <= 0.8
            else:
                r = np.random.rand(1) <= 0.1
            rain[idx] = r

        # decision to take umbrella
        for idx, fs in enumerate(zip(forecast, seen)):
            f, s = fs
            if s:  # saw forecast
                u = f
            else: # did not see forecase
                u = np.random.rand(1) <= 0.5
            umbrella[idx] = u

        df = pd.DataFrame({'Seen': seen, 'Forecast': forecast, 'Umbrella': umbrella,
                           'Rain': rain})

        # Part 1: One day, Victor missed the forecast and it rained. What is the probability that the forecast was “rain"?
        num_rain = np.sum(df.Rain)
        num_forecast_rain = np.sum(df.Forecast & df.Rain)
        prob_forecast_given_rain = num_forecast_rain/num_rain

        print('Prob of forecast=rain given rain: {0}'.format(prob_forecast_given_rain))
        # **Part 2**: Victor misses the morning forecast with probability 0.2 on any day in the year. If he misses the forecast, Victor will flip a fair coin to decide whether to carry an umbrella. (We assume that the result of the coin flip is independent from the forecast and the weather.) On any day he sees the forecast, if it says “rain" he will always carry an umbrella, and if it says “no rain" he will not carry an umbrella. Let U be the event that “Victor is carrying an umbrella", and let N be the event that the forecast is “no rain". Are events U and N independent?
        # Probability of U
        u_prob = np.sum(df.Umbrella == True)/N
        f_prob = np.sum(df.Forecast == True)/N
        uf_prob = np.sum(df.Umbrella & df.Forecast)/N
        uf_prod_prob = u_prob * f_prob
        print("U: {0:.2f}, F: {1:.2f}: U&F: {2:.2f}".format(u_prob, f_prob, uf_prob))
        print("U*F: {0:.2f}".format(uf_prod_prob))
        uf = .2*.8 + .5*.2*.2
        print(uf)
        # Victor is carrying an umbrella and it is not raining. What is the probability that he saw the forecast?
        num_umb_norain = np.sum(df.Umbrella & ~df.Rain)
        num_umb_norain_seen = np.sum([df.Umbrella & ~df.Rain & df.Seen])
        seen_prob = num_umb_norain_seen/num_umb_norain

        print('Prob. of seen {0}'.format(seen_prob))
        num=0.2*.2*.8
        den = num + (.5*.2*.2 + .5*.9*.8)*.2
        num/den

    # def rainProbModel():
    #     model = BayesianModel([('', 'F')])
    #     cpd_t1 = TabularCPD('T1', 2, [[0.9, 0.05],
    #                                   [0.1, 0.95]],
    #                         evidence=['A'], evidence_card=[2])
    #     cpd_t1 = TabularCPD('T1', 2, [[0.9, 0.05],
    #                                   [0.1, 0.95]],
    #                         evidence=['A'], evidence_card=[2])

class Dice:
    def three_sides(self):
        num_simu = 15000

        xpt = np.random.choice([1, 2, 3], size=(num_simu, 6), p=[0.5, 0.25, 0.25])
        df_xpt = pd.DataFrame(xpt)
        # count row by row
        # https://goo.gl/svhSTC
        df = df_xpt.apply(pd.Series.value_counts, axis=1).fillna(0)
        df = df.rename(columns={1: 'N1', 2: 'N2', 3: 'N3'})
        df.head()
        num = df[df.N3 == 2].shape[0]
        den = df.shape[0]

        print(num/den)
        # comb(6, 2) * (1/4)**2 * (3/4)**4

    def largest_face(f, x_max):
    # inputs: m is a list of integers and m_max is an integer
    # output: a variable of type 'float'
    # Example: Here we want to get the probability of getting largest face as 2 for two dices.
    # That should be 3 combinations out of total 36 combinations : 1,2 2,1, 2,2
    # According to formula : P(2)= (2/6)^2 - (1/6)^2 = 3/36
        return np.prod([x_max/float(n) for n in f if x_max <= n]) - np.prod([(x_max - 1) / float(n) for n in f if x_max <= n])

    def constrained_compositions(n, m):
        # inputs: n is of type 'int' and m is a list of integers
        # output: a set of tuples

        k = len(m)
        parts = set()
        if k == n:
            if 1 <= min(m):
                parts.add((1,)*n)
        if k == 1:
            if n <= m[0]:
                parts.add((n,))
        else:
            for x in range(1, min(n-k+2,m[0]+1)):
                for y in constrained_compositions(n-x, m[1:]):
                    parts.add((x,)+y)
        return parts

    # modify this cell

    def face_sum(m, s):
        # inputs: m is list of integers and s is an integer
        # output: a variable of type 'float'
        # Example: Here we want to see to get the probability of largest face summing up to the number provided
        # As for [2,2], we have (1,1),(1,2),(2,1),(2,2) as all possible combinations of largest faces
        # For getting 3 as sum, we have its probability as 2/4 = 0.5
        l1= len(constrained_compositions(s,m))
        l2=1
        for i in m:
            l2= i*l2
        probability= l1/l2
        return probability

    def test_facesum(self):
        assert sum(abs( Dice.face_sum(range(1,10),20) - 0.03037092151675485  )) < 10**-5

    def compositions(k, n):
        # inputs: k and n are of type 'int'
        # output: a set of tuples
        if k == 1:
            return {(n,)}
        else:
            s = set()
            for i in range(1, n):
                for j in compositions(k - 1, n - i): #i + n-i = n
                    s.add((i,) + j)
            return s

    def constrained_sum_compositions(n, m):
        """
            constrained_sum_compositions(9, [1, 2, 3, 4, 5])
        :param m:
        :return:
        """
        # inputs: n is of type 'int' and m is a list of integers
        # output: a set of tuples
        k = len(m)
        s = set()
        for c in Dice.compositions(k, n):
            if sum([c[i] <= m[i] for i in range(k)]) == k: #taking the sets of all comb. which are less than equal to the given
                s.add(c)
        return s

    def test_sum_list(self):
        print(Dice.constrained_sum_compositions(9, [1, 2, 3, 4, 5]))

class DogSearch:
    '''
    A cog in a machine
    {'a': 0.25, 'b': 0.15}

    prob_a = input("The chance found in a:")
    prob_b = input("The chance found in b:")
    Forest_a = input("The chance dog lost in a:")
    Forest_b = 1 - float(Forest_a)

    prob = dict()
    prob['a'] = prob.get('a', 0)  + float(prob_a)
    prob['b'] = prob.get('b', 0)  + float(prob_b)

    N = 5000
    # 0.4, 0.6
    forest = np.random.choice(['a', 'b'], size=N, p=[Forest_a, Forest_b])
    # unique, counts = np.unique(forest, return_counts=True)
    # dict_num = dict(zip(unique, counts))
    # print(dict_num)
    #
    found_a = DogSearch.sim_search(lost_in=forest, look_in='a', prob_found=prob)
    found_b = DogSearch.sim_search(lost_in=forest, look_in='b', prob_found=prob)

    df = pd.DataFrame({'Forest': forest, 'Found_a': found_a, 'Found_b': found_b})
    prob_a = np.sum(df.Found_a==True)/N
    prob_b = np.sum(df.Found_b==True)/N

    print('Prob of finding dog in A: {0}'.format(prob_a))
    print('Prob of finding dog in B: {0}'.format(prob_b))

    np.random.rand(1)
    theory_a = 0.4*.25 + 0.6*0
    theory_b = 0.4*0 + 0.6*.15
    print((theory_a, theory_b))

    ## Oscar flips a fair coin to determine where to look on the first day and finds the dog on the first day. What is the probability that he looked in forest A?
    half_N = int(N/2)
    forest = np.random.choice(['a', 'b'], size=half_N, p=[0.4, 0.6])
    found_a = sim_search(lost_in=forest, look_in='a')
    found_b = sim_search(lost_in=forest, look_in='b')

    df_a = pd.DataFrame({'Forest': forest, 'Look':'a', 'Found':found_a})
    df_b = pd.DataFrame({'Forest': forest, 'Look': 'b', 'Found':found_b})
    df = pd.concat((df_a, df_b))
    df[df.Found==True]['Look'].value_counts(normalize=True)

    ## # d) Oscar decides to look in forest A for the first two days. What is the probability that he finds his dog alive for the first time on the second day?
    forest = np.random.choice(['a', 'b'], size=N, p=[.4, .6])

    # simulate search in forest
    found_1 = sim_search(lost_in=forest, look_in='a')
    found_2 = sim_search(lost_in=forest, look_in='a')

    # simulate dog is alive
    alive_1 = np.random.rand(N) <= 2/2
    alive_2 = np.random.rand(N) <= 2/3


    df = pd.DataFrame({'Forest': forest,
                       'F1': found_1, 'F2': found_2,
                       'A1': alive_1, 'A2': alive_2})
    fin_df = df[(df.F1==False) & (df.F2==True) & (df.A2==True)]

    fin_df.shape[0]/N

    ##e) Oscar decides to look in forest A for the first two days. Given that he did not find his dog on the first day, find the probability that he does not find his dog dead on the second day.
    forest = np.random.choice(['a', 'b'], size=N, p=[.4, .6])

    # simulate search in forest
    found_1 = sim_search(lost_in=forest, look_in='a')
    found_2 = sim_search(lost_in=forest, look_in='a')

    # simulate dog is alive
    alive_1 = np.random.rand(N) <= 2/2
    alive_2 = np.random.rand(N) <= 2/3


    df = pd.DataFrame({'Forest': forest,
                       'F1': found_1, 'F2': found_2,
                       'A1': alive_1, 'A2': alive_2})
    given_df = df[(df.F1 == False)]
    find_dead_df = given_df[(given_df.A2==False) & (given_df.F2==True)]
    find_dead_df.shape

    prob_e = 1 - find_dead_df.shape[0]/given_df.shape[0]
    prob_e
    ## Theory
    p_not_f1 = 0.4*.75 + 0.6*1
    p_f2 = 0.4*.25

    num = p_not_f1 * 1/3 * p_f2
    den = p_not_f1
    ans = 1- num/den

    print(ans)

    forest = np.random.choice(['a', 'b'], size=N, p=[.4, .6])

    # # simulate search in forest
    # found_1 = sim_search(lost_in=forest, look_in='a')
    # found_2 = sim_search(lost_in=forest, look_in='a')
    # found_3 = sim_search(lost_in=forest, look_in='a')
    # found_4 = sim_search(lost_in=forest, look_in='b')
    #
    # # simulate dog is alive
    # alive_1 = np.random.rand(N) <= 2/2
    # alive_2 = np.random.rand(N) <= 2/3
    # alive_3 = np.random.rand(N) <= 2/4
    # alive_4 = np.random.rand(N) <= 2/5
    #
    # df = pd.DataFrame({'Forest': forest,
    #                    'F1': found_1, 'F2': found_2, 'F3': found_3, 'F4': found_4,
    #                    'A1': alive_1, 'A2': alive_2, 'A3': alive_3, 'A4': alive_4})
    # dog alive on all days
    # df['A1_A4'] = df.A1 & df.A2 & df.A3 & df.A4
    #
    # f4_df = df[(df.F4==True)]
    # f4_a1t04_df = f4_df[f4_df.A1_A4 == True]
    #
    # print(f4_a1t04_df.shape[0]/f4_df.shape[0])
    # print(f4_a1t04_df.shape[0]/N)
    my_guess2 = 1 * 2/3 * 1/2 * 2/5 * 0.6 * 0.15
    '''

    def sim_search(lost_in, look_in, prob_found):
        """ Simulate a search for dog"""
        N = lost_in.shape[0]
        prob_dict = prob_found  # prob of found
        res = np.array([False]*N)
        for idx, forest in enumerate(lost_in):
            if forest == look_in:
                r = np.random.rand(1) <= prob_dict[forest]
            else:
                r = False
            res[idx] = r
        return res



# def seq_sum(n):
#     """ input: n, generate a sequence of n random coin flips
#         output: return the number of heads
#         Hint: For simplicity, use 1,0 to represent head,tails
#     """
#     total_heads = 0
#     total_tails = 0
#     count = 0
#     while count < n:
#         coin = random.randint(0, 1)
#         if coin == 1:
#             total_heads += 1
#             count += 1
#
#         elif coin == 0:
#             total_tails += 1
#             count += 1
#
#     return total_heads

def test_seq_sum():
    '''
    DogSearch.test_seq_sum()
    :return:
    '''
    # x = DogSearch.seq_sum(100)
    # print(pd.unique([DogSearch.seq_sum(2) for x in  range(0,200)]))
    assert pd.unique([seq_sum(2) for x in  range(0,200)]).tolist() == [0, 1, 2]

def estimate_prob(n,k1,k2,m,Log):
    """Estimate the probability that n flips of a fair coin result in k1 to k2 heads
         n: the number of coin flips (length of the sequence)
         k1,k2: the trial is successful if the number of heads is
                between k1 and k2-1
         m: the number of trials (number of sequences of length n)

         output: the estimated probability
         """
    successful_trial = 0
    for i in range(m):
        x = seq_sum(n,Log)
        if x>k1 and x<k2:
            successful_trial+=1
        elif x<k1 or x>k2:
            successful_trial+=0
    estimated_probability = successful_trial/m
    return estimated_probability

def test_estimate_prob(Log):
    """
    Log=[]
    test_estimate_prob(Log)
    :param Log:
    :return:
    """
    x = estimate_prob(100,40,60,1000,Log)
    print(x)
    assert 'float' in str(type(x))

def calc_prob(n,k1,k2):
    """Calculate the probability using a normal approximation"""
    n=float(n)
    k1=float(k1)
    k2=float(k2)
    z1=(k1-0.5*n)/(sqrt(n)/2)
    z2=(k2-0.5*n)/(sqrt(n)/2)
    return (erf(z2/sqrt(2))-erf(z1/sqrt(2)))/2


def evaluate(n,q1,q2,m,r=100):
    """Run calc_range many times and test whether the estimates are consistent with calc_prob"""
    k1=int(q1*n)
    k2=int(q2*n)
    p=calc_prob(n,k1,k2)
    std=sqrt(p*(1-p)/m)
    print("computed prob=%5.3f, std=%5.3f" %(p,std))

    L=[estimate_prob(n,k1,k2,m) for i in range(r)]
    med=np.median(L)
    print("ran estimator %r times, with parameters n=%d,k1=%d,k2=%d,m=%d" %(r,n,k1,k2,m))
    print('median of estimates=%5.3f, error of median estimator=%5.3f, std= %f5.3'%(med,med-p,std))
    return L,med,p,std,abs((med-p)/std)

def test_report_assert(n,q1,q2,m,r=100):
    k1=int(q1*n)
    k2=int(q2*n)
    L,med,p,std,norm_err=evaluate(n,q1,q2,m,r=100)
    plt.hist(L)
    plt.plot([p,p],plt.ylim(),'r',label='true prob')
    plt.plot([med,med],plt.ylim(),'k',label='median of %d estimates'%r)
    mid_y= np.mean(plt.ylim())
    plt.plot([p-std,p+std],[mid_y,mid_y],'g',label='+-std')
    plt.legend()
    print('normalized error of median=',norm_err,'should be <1.0')
    plt.title('r=%d,n=%d,k1=%d,k2=%d,m=%d,\nnorm_err=%4.3f'%(r,n,k1,k2,m,norm_err))
    assert norm_err<1.0

def test_1():
    # checking functions

    m=100
    i=1
    plt.figure(figsize=[10,12])
    for n in [100,1000]:
        for q1,q2 in [(0.4,0.6),(0.55,1.00),(0.47,0.499)]:
            fig= plt.subplot(3,2,i)
            print('#### test no.',i)
            i+=1
            test_report_assert(n,q1,q2,m,r=100)
    plt.tight_layout()

def seq_sum(n,Log):
    # s=2*(random.rand(n)>0.5)-1
    s=sum(random.rand(n)>0.5)
    Log.append((n,s))
    return s


def test_2():
# checking functions
    n,k1,k2,m = 100,45,50,1000
    Log=[]
    for r in range(10):
        a=estimate_prob(n,k1,k2,m,Log)
        b=float(sum([(s>=k1 and s<k2) for n,s in Log]))/m
        n_correct=sum(nn==100 for nn,s in Log)
        assert a==b, "estimate is incorrect. should be %4f, instead is %4f"%(b,a)
        assert m==len(Log), 'should call seq_sum %d times, called it %d times'%(m,len(Log))
        assert m==n_correct, 'the parameter n should be %d but sometimes it was not.'%n

    print("all good!")
# modify this cell

def compositions(k, n):
    # inputs: k and n are of type 'int'
    # output: a set of tuples
    if k == 1:
        return {(n,)}
    else:
        s = set()
        for i in range(1, n):
            for j in compositions(k - 1, n - i): #i + n-i = n
                s.add((i,) + j)
        return s
def constrained_compositions(n, m):
    '''
    Constrain compositions sum up to n
    :param n:
    :param m:
    :return:
    '''
    # inputs: n is of type 'int' and m is a list of integers
    # output: a set of tuples
    k = len(m)
    s = set()
    for c in compositions(k, n):
        if sum([c[i] <= m[i] for i in range(k)]) == k: #taking the sets of all comb. which are less than equal to the given
            s.add(c)
    return s

def test_composition():
    func_out = compositions(2, 8)
    assert type(func_out).__name__ == "set"
    assert func_out == {(1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1)}

def test_constrain_comp():
    # Check Function
    func_out = constrained_compositions(7, [1,4,4])
    assert type(func_out).__name__ == "set"
    assert constrained_compositions(7, [1,4,4]) == {(1, 2, 4), (1, 3, 3), (1, 4, 2)}

def permute():
    A = {1, 2, 3, 4}
    k = 3
    # Print all the k-permutations of A
    n = len(A)
    permute_k = list(itertools.permutations(A, k))
    print("%i-permutations of %s:  " %(k,A))
    for i in permute_k:
        print(i)
    print("Size = ", "%i!/(%i-%i)! = " %(n,n,k), len(permute_k))

def combination():
    A = {1, 2, 3, 4}
    k = 2
    # Print all the k-combinations of A
    choose_k = list(itertools.combinations(A,k))
    print("%i-combinations of %s:  " %(k,A))
    for i in choose_k:
        print(i)
    print("Number of combinations = %i!/(%i!(%i-%i)!) = %i" %(n,k,n,k,len(choose_k)  ))

if __name__ == '__main__':
    # pass

    test_2()
    # permute()
    # Coupon_collector.Coupon(0)

    # g = np.linspace(0,np.pi,num=5)
    # print(g)
    # g[3:] += np.pi

    # print(np.unwrap(g))
    # coin.test_toss2()

    # Dice.test_sum_list()