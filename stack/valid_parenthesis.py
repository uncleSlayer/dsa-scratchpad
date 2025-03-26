input_one = "({[]})"
input_two = "({[})"

def check_if_parenthesis_is_valid(parenthesis):

    opposite_parenthesis = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    parenthesis_tracker_stack = []

    for parenth in parenthesis:

        if parenth not in opposite_parenthesis:
            parenthesis_tracker_stack.append(parenth)

        else:

            if parenthesis_tracker_stack and opposite_parenthesis[parenth] != parenthesis_tracker_stack.pop():
                break;
    

    return len(parenthesis_tracker_stack) == 0



print(check_if_parenthesis_is_valid(input_two))
            
    
