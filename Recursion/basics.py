def rev(l, r, arr):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    rev(l + 1, r - 1, arr)


def rev2(i, arr):
    if i > len(arr) // 2:
        return arr
    arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
    return rev2(i + 1, arr)


def palindrome(i, arr):
    if i > len(arr) // 2:
        return True
    if arr[i] != arr[len(arr) - 1 - i]:
        return False
    return palindrome(i + 1, arr)


def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def bs(arr, l, r, target):
    mid = (l + r) // 2
    if l >= r:
        return -1
    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return bs(arr, mid + 1, r, target)
    else:
        return bs(arr, l, mid - 1, target)


arr = [1, 2, 3, 4]
# rev(0, len(arr)-1, arr)
# print(rev2(0, arr))
# print(palindrome(0, arr))
# print(fib(6))
print(bs(arr, 0, len(arr), 7))
