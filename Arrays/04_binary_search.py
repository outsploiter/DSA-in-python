def binary_search(arr, target):
    start = 0
    end = len(arr)-1
    while start <= end:
        middle = start + ((end - start) // 2)
        if target == arr[middle]:
            return middle
        elif target > arr[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return -1


array = [2, 6, 9, 10, 17, 25, 48, 51]
target = 56
ans = binary_search(array, target)
print(f'Target found in index {ans}')