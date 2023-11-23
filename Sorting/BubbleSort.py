def bubble_sort(arr):
    n = len(arr)
    counter = 0
    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            counter += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, counter


def bubble_sort_optimized(arr):
    n = len(arr)
    counter = 0
    for i in range(n - 1, 0, -1):
        swap_flag = False
        for j in range(0, i):
            counter += 1
            if arr[j] > arr[j + 1]:
                swap_flag = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swap_flag:
            break
    return arr, counter


arr = range(0, 100)
print(bubble_sort(arr))
arr = range(0, 100)
print(bubble_sort_optimized(arr))
