def find_freq(arr):
    # to find frequency of the numbers in array (0to9)
    hash = {}
    for i in arr:
        hash[i] = hash.get(i, 0) + 1
    return hash


def find_freq_str(str):
    # to find the frequency of the chars in string (a to z)
    hash = {}
    for i in str:
        hash[i] = hash.get(i, 0) + 1
    return hash


def find_max_freq(hash):
    max = 0
    value = None
    for i in range(len(hash)):
        if hash[i] > max:
            value = i
            max = hash[i]

    return value, max


arr = [1, 2, 3, 1, 2, 4, 4, 4, 4, 4, 4, 4]
arr_freq = find_freq(arr)
str = "aabcda"
str_freq = find_freq_str(str)
print(str_freq)
# print(find_max_freq(arr_freq))
