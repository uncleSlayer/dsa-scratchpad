arr = [2, 4, 5, 6, 7, 20, 33, 45, 40, 3, 1, 0]


"""
For this question I wrong the following answer which solves the question but throws TLE in leetcode.
So there has to be a more optimized solution.


If you see I've done left <= right in this case but this is unncessary.
In a mountain array there is always a peak element.
Left and Right will be same only if the peak element is the last element of the array.
If peak element is not the last element then this is not a mountain array anymore.
"""


def peakIndexInMountainArray(arr):

    left, right = 0, len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return mid

        else:
            if arr[mid - 1] > arr[mid] and arr[mid] > arr[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1


"""
This is the optimized solution.

Point is if next element to mid is greater than mid, that means peak is on the right side.
Otherwise the peak can either be mid itself because we don't know if the previous element to mid is greater than mid or not. So we do right = mid whereas left = mid + 1

Why will left == right in the end?
Because in the first place in the while loop we are not checking if left == right. so at one point they will become same. That is the peak.
"""


def peakIndexInMountainArray(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left  # or right — same at this point


print(peakIndexInMountainArray(arr))
