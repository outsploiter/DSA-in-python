def binary_search(arr, target, start, end):
    while start <= end:
        middle = start + ((end - start) // 2)
        if target == arr[middle]:
            return middle
        elif target > arr[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return -1


# def binary_search_order_automated(arr, target):
#     start = 0
#     end = len(arr) - 1
#     is_asc = None
#     if arr[start] < arr[end]:
#         is_asc = True
#     else:
#         is_asc = False
#     while start <= end:
#         middle = start + ((end - start) // 2)
#         if target == arr[middle]:
#             return middle
#         if is_asc:
#             if target > arr[middle]:
#                 start = middle + 1
#             else:
#                 end = middle - 1
#         else:
#             if target < arr[middle]:
#                 start = middle + 1
#             else:
#                 end = middle - 1
#     return -1


def binary_infinite_array(arr, target):
    start = 0
    end = 1
    while target > arr[end]:
        temp = end
        l = (end - start) + 1
        end = (l * 2) + temp
        start = temp + 1
    return binary_search(arr, target, start, end)


if __name__ == '__main__':
    array = [2, 6, 9, 10, 17, 25, 48, 51, 87, 98, 100, 102, 120, 130 ,140]
    rev_array = [51, 48, 25, 17, 10, 9, 6, 2]
    target = 100
    ans = binary_infinite_array(array, target)
    print(f'Target found in index {ans}')
