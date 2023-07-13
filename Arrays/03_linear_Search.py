def linear_search_index(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def linear_search_foreach(arr, x):
    for i in arr:
        if i == x:
            return 'Found'
    return 'Not Found'


arr = [10, 13, 4, 5, 7, 8, 2, 1, 34]
index = linear_search_index(arr, 2)
print(f'\n\nIndex linear search found element (2) at index : {index}\n')
index = linear_search_index(arr, 58)
print(f'Index linear search found element (58) at index : {index}\n\n')

print(f'ForEach Search for element (2) in array : {linear_search_foreach(arr, 2)}\n')
print(f'ForEach Search for element (58) in array : {linear_search_foreach(arr, 58)}\n\n')
