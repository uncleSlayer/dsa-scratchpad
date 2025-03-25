input = [1, 2, 4, 4, 2, 1]
input_2 = [1, 2, 4, 2, 1]
input_3 = [1, 2, 4, 5, 1]

def is_palindrome(nums: list[int]) -> bool:

    left, right = 0, len(nums) - 1

    is_nums_palindrome = True

    while left <= right:

        if nums[left] != nums[right]:
            is_nums_palindrome = False
            break;
    
        left += 1
        right -= 1

    return is_nums_palindrome


print(is_palindrome(input_3))