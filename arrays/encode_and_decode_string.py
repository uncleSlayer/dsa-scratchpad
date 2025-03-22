input = ["neet", "code", "love", "you"]

def encode(input):

    output = ""

    for word in input:

        output += str(len(word)) + "$" + word

    return output


def decode(encoded_string: str):
    answer = []

    for index, character in enumerate(encoded_string):
        
        if character == "$" and encoded_string[index - 1].isdigit():

            word_length = ""
            word_length_counter = index

            # this while loop makes sure that the length of the string, even if more than two digits, is accounted.
            while encoded_string[word_length_counter - 1].isdigit():
                word_length += encoded_string[word_length_counter - 1]
                word_length_counter-=1

            word_length = int(word_length[::-1])

            answer.append(encoded_string[index + 1 : index + word_length + 1])

    return answer

print(decode(encode(input)))