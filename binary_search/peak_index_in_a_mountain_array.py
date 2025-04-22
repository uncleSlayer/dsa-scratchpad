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
"""


def optimizedPeakIndexInMountainArray(arr):

    """
    Let's say arr[mid] > arr[mid - 1]
    """

    left, right = 0, len(arr) - 1
    
    ans = 0

    while left < right:

        mid = (left + right) // 2

        if arr[mid] > arr[mid - 1]:
            if arr[mid] > arr[ans]:
                ans = mid
            left = mid + 1
        else:
            if arr[mid] > arr[ans]:
                ans = mid
            right = mid

    return ans


print(optimizedPeakIndexInMountainArray(arr))
