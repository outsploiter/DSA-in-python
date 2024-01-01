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


arr = [9,52,4,3,9,10,20,45,7,4,4,6,6,6,0]
quickSort(arr, 0, len(arr) - 1)
print(arr)
