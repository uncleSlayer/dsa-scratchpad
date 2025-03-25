input_string = ["h", "e", "l", "l", "o"]

def reverse_string(input):

    """
    Ok. This works. 
    """

    left, right = 0, len(input) - 1

    while left < right:

        temp_left_storage = input[left]

        input[left] = input[right]

        input[right] = temp_left_storage

        left += 1
        right -= 1

    return input


def reverse_string_with_tuple_unpacking(input):

    """
    claude taught me this chad move lol.
    this way you don't have to manage one extra temporary variable 
    """

    left, right = 0, len(input) - 1

    while left < right:

        input[left], input[right] = input[right], input[left]

        left += 1
        right -= 1

    return input


# print(reverse_string(input_string))
print(reverse_string_with_tuple_unpacking(input_string))