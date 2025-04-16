arr = [3, 5, 7, 7, 7, 7, 8, 8, 10]

left_most_index = None
right_most_index = None


def binary_search(lis: list[int], target: int, side: str):

    global left_most_index, right_most_index
    start, end = 0, len(lis) - 1
    result = None

    while start <= end:

        mid = (start + end) // 2

        if lis[mid] == target:

            result = mid

            if side == "left":

                end = mid - 1

            elif side == "right":

                start = mid + 1

        elif lis[mid] > target:

            end = mid - 1

        elif lis[mid] < target:

            start = mid + 1

        if side == "left" and result is not None:
            left_most_index = result

        elif side == "right" and result is not None:
            right_most_index = result


binary_search(arr, 7, "left")

binary_search(arr, 7, "right")

print([left_most_index, right_most_index])
