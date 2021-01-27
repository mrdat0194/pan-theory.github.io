#!/bin/python3
import os

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    '''
    swap to get a increasing order
    Given array
    After swapping  we get 1 3 4 2
    After swapping  we get 1 4 3 2
    After swapping  we get 1 2 3 4
    So, we need a minimum of  swaps to sort the array in ascending order
    :param arr:
    :return:
    '''
    ref_arr = sorted(arr)
    index_dict = {v: i for i,v in enumerate(arr)}
    swaps = 0
    
    for i,v in enumerate(arr):
        correct_value = ref_arr[i]
        if v != correct_value:
            to_swap_ix = index_dict[correct_value]
            arr[to_swap_ix],arr[i] = arr[i], arr[to_swap_ix]
            index_dict[v] = to_swap_ix
            index_dict[correct_value] = i
            swaps += 1
    return swaps

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    output = os.path.join(BASE_DIR, "output_miniswap.txt")
    if os.path.exists(output):
        f = open(output, "r+")
    else:
        f = open(output, "w")

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    f.write(str(res) + '\n')

    f.close()
# 4
# 4 3 1 2
