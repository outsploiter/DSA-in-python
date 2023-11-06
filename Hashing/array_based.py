def find_freq(arr):
    # to find frequency of the numbers in array (0to9)
    hash = [0] * 10
    for i in arr:
        hash[i] += 1
    return hash


def find_freq_str(str):
    # to find the frequency of the chars in string (a to z)
    hash = [0] * 26  # for a to z
    for i in str:
        hash[ord(i) - ord('a')] += 1
    return hash


def find_max_freq(hash):
    max = 0
    value = None
    for i in range(len(hash)):
        if hash[i] > max:
            value = i
            max = hash[i]

    return value, max


def find_min_freq():
    pass


def two_sum():
    # Solve two sum from leetcode
    pass


arr = [1, 2, 3, 1, 2, 4, 4, 4, 4, 4, 4, 4]
arr_freq = find_freq(arr)
str = "aabcda"
str_freq = find_freq_str(str)
print(find_max_freq(arr_freq))
