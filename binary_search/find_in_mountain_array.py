arr = [1, 2, 3, 4, 6, 5, 1]
target = 4


def find_peak_of_mountain_array(arr):

    left, right = 0, len(arr) - 1

    while left < right:

        mid = (left + right) // 2

        if arr[mid + 1] > arr[mid]:
            left = mid + 1
        else:
            right = mid

    return left


def binary_search(arr, target):

    left, right = 0, len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


peak = find_peak_of_mountain_array(arr)

if arr[peak] == target:
    print(peak)

else:

    left = binary_search(arr[:peak], target)
    right = binary_search(arr[peak + 1:], target)

    if left != -1:
        print(left)
    elif right != -1:
        print(right + peak + 1)
    else:
        print(-1)
