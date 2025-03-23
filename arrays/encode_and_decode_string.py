input = ["neet", "code", "love", "you"]

def encode(input):

    output = ""

    for word in input:

        output += str(len(word)) + "$" + word

    return output


"""
    there is a problem with the following code(an edge case):

    input = ["hello3", "cup"]

    so in this case the encoded string will be 6$hello33$cup

    now here the problem is when you go backwards from the $ we have 33 before $cup, which means it indicates that length for the next word is 33. which is wrong.

"""
def decode(encoded_string: str):
    answer = []

    for index, character in enumerate(encoded_string):
        
        if character == "$" and encoded_string[index - 1].isdigit():

            word_length = ""
            word_length_counter = index

            while encoded_string[word_length_counter - 1].isdigit():
                word_length += encoded_string[word_length_counter - 1]
                word_length_counter-=1

            word_length = int(word_length[::-1])

            answer.append(encoded_string[index + 1 : index + word_length + 1])

    return answer

# print(decode(encode(input)))

"""
    correct approach
"""

def decode(encoded_string: str):

    i = 0

    decoded_list: list[str] = []

    """ 
    here we are looping through the characters of the encoded string and i is the left pointer.
    but why do we do i < len(encoded_string) and not i <= len(encoded_string) ?
    because i is always the first index of the word length and j is the last index.
    whenever we find a $ with j that means there is a word after $ and i and j will both will be the index before the word itself.
    so i and j they both will never cross the length of the encoded string.

    when we encounter the last word, we append the value to decoded_list and after that we increase the value of i which exceeds the encoded_string's length and the program ends there 
    """

    while i < len(encoded_string):

        """ here we are looping through the word length as a string only till we get $ """
        j = i

        while encoded_string[j]!= "$":

            j += 1

        """ at this point j pointer is on $ itself because we come out of the loop when we encounter $ """

        """ i is still in the first posiiton and j on the $ so the word length will start from i to the index just before the $ """  
        word_length = int(encoded_string[i:j])

        """ so the word will start from the next index from j (which is $ in this case) till the index of j + word_length + 1 """
        decoded_list.append(encoded_string[j+1: j+word_length+1])

        """ then we increase the value of i to j + word_length + 1 """
        i = j + word_length + 1

    return decoded_list
    


print(decode(encode(input)))