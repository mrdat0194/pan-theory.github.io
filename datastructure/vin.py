# Question 1. Given an array of integer numbers, which are already sorted. E.g., A = [1,2,3,3,3,4,4,5,5,6]
# •	Find the mode of the array
# •	Provide the time complexity and space complexity of the array, and your reasoning
# •	Note: write your own function using the basic data structure of your language, please avoid the provided available functions from external lib
# Question 2. Given the stock value of VIC in n continuous days as an array, e.g., A = [p1, p2, p3, ..., pn]
# Please find a single buying date and a single selling date so that the the buyer could get the best profit.
# Knowing that you have to buy before selling anything.

def ModedSortedArray(arr):
    length = len(arr)
    count = 1
    tempMode = arr[0]
    tempCount = 1
    modes = 0
    for i in range(1,length):
        if tempMode == arr[i]:
            tempCount += 1
            if tempCount > count:
                modes = tempMode
                count = tempCount
        else:
            tempMode = arr[i]
            tempCount = 1
    return modes

def ModedArray(arr):
    count = 1
    tempCount = 0
    modes = arr[0]
    for i in range(len(arr) - 1):
        tempMode = arr[i]
        print(tempMode)
        for j in range(1, len(arr)):
            if tempMode == arr[j]:
                tempCount += 1
        if tempCount > count:
            modes = tempMode
            count = tempCount
    return modes

def maxProfitWithKTransactions(prices, k):
    # Time: O(kn) | Space: O(n)
    prev_trans = [0 for _ in prices]
    curr_trans = []
    for t in range(k):
        curr_trans = [0]
        max_diff = float('-inf')

        for i in range(1, len(prices)):
            max_diff = max(max_diff, prev_trans[i - 1] - prices[i - 1])
            curr_trans.append(max(curr_trans[i - 1], prices[i] + max_diff))
        prev_trans = curr_trans[:]
        print(curr_trans)
    return curr_trans[-1]

def max_profit(price):
    max_profit = 0
    for day_buy in range(len(price)-1):
        for day_sell in range(day_buy+1, len(price)):
            profit_amt = price[day_sell] - price[day_buy]
            if profit_amt > max_profit:
                day_buy_best = day_buy
                day_sell_best = day_sell
                max_profit = profit_amt
    print(f"Buy at day {day_buy_best +1},Sell at {day_sell_best+1}")

# Given an array of positive integers, divide the array into two subsets such that the difference between the sum of the subsets is as small as possible.
#
# For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which has a difference of 5, which is the smallest possible difference.

def get_diff(s1, s1_sum, s2, s2_sum, score):
    min_diff, min_cand = score, None
    for i, num in enumerate(s1):

        new_s1_sum, new_s2_sum = s1_sum - num, s2_sum + num
        new_score = abs(new_s1_sum - new_s2_sum)
        if new_score < min_diff:
            min_diff = new_score
            min_cand = (s1[:i] + s1[i + 1:], new_s1_sum,
                        s2 + [num], new_s2_sum)
    if not min_cand:
        return (set(s1), set(s2))

    return get_diff(min_cand[0], min_cand[1], min_cand[2], min_cand[3], min_diff)


def divide_numbers(nums):
    sum_nums = sum(nums)
    best_sets = get_diff(nums.copy(), sum_nums, [], 0, sum_nums)

    return best_sets
# Tests
assert divide_numbers([5, 10, 15, 20, 25]) == ({5, 15, 20}, {10, 25})
assert divide_numbers([5, 10, 15, 20]) == ({10, 15}, {20, 5})

#dynamic programming FIB

def fib_dn(N, memo={0:1,1:1}):
    if N not in memo:
        memo[N] = fib_dn(N-1,memo) + fib_dn(N-2,memo)
    return memo[N]

#intersect rectangle
# Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.
#
# For example, given the following rectangles:
#
# {
#     "top_left": (1, 4),
#     "dimensions": (3, 3) # width, height
# }
# and
#
# {
#     "top_left": (0, 5),
#     "dimensions": (4, 3) # width, height
# }
# return 6.

def rectangles(rec1, rec2):
    left_x = max(rec1["top_left"][0], rec2["top_left"][0])
    right_x = min(rec1["top_left"][0] + rec1["dimensions"][0], rec2["top_left"][0] + rec2["dimensions"][0])

    top_y = min(rec1["top_left"][1], rec2["top_left"][1])
    bottom_y = max(rec1["top_left"][1] - rec1["dimensions"][1], rec2["top_left"][1] - rec2["dimensions"][1])

    if left_x > right_x or bottom_y > top_y:
        return 0

    return (right_x - left_x) * (top_y - bottom_y)
if __name__ == '__main__':
    # mode([1, 1, 2, 3, 3, 3, 3, 4])
    data = [1, 1, 2,2,2,2,2,2, 3, 3, 3, 3, 4,4,4,4,4]
    stock = [225, 224, 407, 221, 259, 403]
    # max_profit(stock)
