def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        minimum = i
        for j in range(i, n):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]

    return arr


arr = [3, 2, 1, 4, 5, 56, 0, 0, 0]
print(selection_sort(arr))
