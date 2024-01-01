def merge(L, R, arr):
    i = 0
    j = 0
    k = 0
    while i<len(L) and j<len(R):
        if L[i] > R[j]:
            arr[k] = R[j]
            j += 1
        else:
            arr[k] = L[i]
            i += 1
        k += 1

    while i<len(L):
        arr[k] = L[i]
        i+=1
        k+=1
    while j<len(R):
        arr[k] = R[j]
        j+=1
        k+=1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        merge(L, R, arr)
    return arr


if __name__ == '__main__':
    array = [6,5,1,2,3]
    print("BEFORE::", array)
    print("AFTER::", merge_sort(array))
