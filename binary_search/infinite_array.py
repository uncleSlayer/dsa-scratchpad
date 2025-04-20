input = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]

target = 9


def binary_search(nums: list[int], target: int):

    left, right = 0, len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def search_infinite_array():

    left, right = 0, 1
    
    while target > input[right]:
        
        arr_len = len(input[left: right + 1])
        left = right + 1
        right = right + (arr_len * 2)
    
    return left + binary_search(input[left : right + 1], target)


print(search_infinite_array())