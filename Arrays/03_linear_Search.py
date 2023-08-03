def linear_search(arr, target):
    for i in range(len(arr)):
        element = arr[i]
        if element == target:
            return i
    return -1

def linear_search_range(arr, target, start, end):
    if start < len(arr)-1:
        for i in range(start, end+1):
            if end > len(arr)-1:
                return -1
            element = arr[i]
            if element == target:
                return i
    return -1

def minimum_search(arr):
    if len(arr) < 1:
        return "invalid arr"
    min_value = 9999999
    for i in range(len(arr)):
        curr_element = arr[i]
        if min_value > curr_element:
            min_value = curr_element
    return min_value

def linear_search_2d(arr, target):
    # for row in arr:
    #     for element in row:
    #         if element == target:
    #             return True
    # return False

    for i in range(len(arr)):
        row = arr[i]
        for j in range(len(row)):
            element = row[j]
            if element == target:
                return i, j
    return -1


def linear_search_2d_max(arr):
    max_value = -9999999
    for i in range(len(arr)):
        row = arr[i]
        for j in range(len(row)):
            curr_element = row[j]
            if max_value < curr_element:
                max_value = curr_element
    return max_value


arr = [
    [2, 4, 6],
    [3, 6, 9],
    [4, 8, 12, 16],
    [7, 9, 13, 970, 103]
]
target = 104


index = linear_search_2d_max(arr)
print(f'minimum element: {index}')