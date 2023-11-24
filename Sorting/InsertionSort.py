def insertion_sort(arr):
    n = len(arr)
    count = 0
    for i in range(1, n):
        for j in range(i, 0, -1):
            count += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr, count


def insertion_sort_opt(arr):
    n = len(arr)
    count = 0
    for i in range(1, n):
        for j in range(i, 0, -1):
            count += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return arr, count


def insertion_sort_while(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


arr = list(range(10, 1, -1))
arr_2 = arr.copy()
arr_3 = arr.copy()
print(insertion_sort(arr))
print(insertion_sort_opt(arr_2))
print(insertion_sort_while(arr_3))
