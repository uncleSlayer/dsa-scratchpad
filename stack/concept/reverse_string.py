input = "hello"

# noob method of doing this
def reverse_input(inp):

    stack = []

    reversed_stack = []

    for character in inp:

        stack.append(character)

    for inp in stack.copy():
        pop_value = stack.pop()

        reversed_stack.append(pop_value)

    return ''.join(reversed_stack)


# print(reverse_input(input))

# chat gpt way. Literally chat gpt is a much better coder than me lol
def reverse_input_with_while_loop(inp):
    
    stack = list(inp)

    reversed_list = []

    while stack:
        reversed_list.append(stack.pop())

    return "".join(reversed_list)


print(reverse_input_with_while_loop(input))