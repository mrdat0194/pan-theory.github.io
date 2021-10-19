def twoSumHashing(num_arr, pair_sum):
    sums = []
    hashTable = {}

    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        if complement in hashTable:
            print("Pair with sum", pair_sum,"is: (", num_arr[i],",",complement,")")
        # print(hashTable)
        hashTable[num_arr[i]] = num_arr[i]
        # print(hashTable)

if __name__ == '__main__':

    # Driver Code
    num_arr = [4, 5, 5, 1, 8]
    pair_sum = 9

    # Calling function
    twoSumHashing(num_arr, pair_sum)