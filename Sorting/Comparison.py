import time
import random
import sys

sys.setrecursionlimit(5000)

def bubbleSort(arr):
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

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i < high:
            i += 1
        while arr[j] > pivot and j > low:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[low] = arr[low], arr[j]
    return j

def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)  # go left
        quickSort(arr, pivot + 1, high)  # go right


if __name__ == '__main__':
    arr_1 = arr_2 = [random.randint(1, 100) for _ in range(10_000)]
    start_time = time.time()
    bubbleSort(arr_1)
    end_time_1 = time.time()
    quickSort(arr_2, 0, len(arr_2)-1)
    end_time_2 = time.time()

    print("Bubble Sort time:", end_time_1 - start_time, "seconds")
    print("Quick Sort time:", end_time_2 - end_time_1, "seconds")