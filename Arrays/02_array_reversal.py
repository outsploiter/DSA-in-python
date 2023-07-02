def reverse_list(arr):
    first = 0
    last = len(arr)-1
    while first < last:
        arr[first], arr[last] = arr[last], arr[first]  # swap
        first += 1  # increase first
        last -= 1  # decrease last
    return arr


if __name__ == '__main__':
    arr1 = [7, 0, 5, 8, 9, 3]
    arr2 = list('PARTY')
    arr3 = []  # boundary case
    arr4 = [1]  # boundary case 2

    print(reverse_list(arr3))
