"""
Problem: Remove duplicates in-place from a sorted array.
- Input: A sorted array of integers
- Goal: Remove duplicates so each unique element appears only once
- Return the number of unique elements
- Example:
  Input: [0,0,1,1,1,2,2,3,3,4]
  Output: 5 (array becomes [0,1,2,3,4,_,_,_,_,_])

Tips:
- Use two pointers: one to iterate, one to track unique elements
- Compare current element with the last unique element
- Modify array in-place


LOL claude asked me this question, and my answer was wrong.
Claude played smart.
"""


input_number_list = [ 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 ]

def remove_duplicates(num_list):

    """
    This was my noob way of removing the duplicates. 
    """

    no_duplicates_containing_list = []

    i = 0

    while i <= len(input_number_list) - 1:

        j = i

        no_duplicates_containing_list.append(num_list[i])
        
        while j <= len(num_list) - 1 and num_list[i] == num_list[j]:
            j += 1

        i = j

    return no_duplicates_containing_list


def remove_duplicates_claude_style(num_list):

    if not num_list:
        return 0

    unique_index = 0

    for number in num_list:

        if number != num_list[unique_index]:

            """ 
            the point is whenever our current number is not matching our unique_index we are moving the uniq_index by one.
            because this is a sorted array that makes sense. the next item will obviously be uniqe and now unique_index is updated with the index of real unique number
            """

            unique_index += 1

            num_list[unique_index] = number

    print(num_list)

    return unique_index + 1


# print(remove_duplicates(input_number_list))
print(remove_duplicates_claude_style(input_number_list))