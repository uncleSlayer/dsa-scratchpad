temperatures = [30,38,30,36,35,40,28]

def get_warmer_temperature_forcast(temperatures):

    result = [0] * len(temperatures)

    past_less_warm_temperature_stack = []

    for current_index, current_temperature in enumerate(temperatures):

        while past_less_warm_temperature_stack and past_less_warm_temperature_stack[-1][1] < current_temperature:

            past_index, past_temperature = past_less_warm_temperature_stack.pop()

            result[past_index] = current_index - past_index

        past_less_warm_temperature_stack.append([current_index, current_temperature])

    return result


print(get_warmer_temperature_forcast(temperatures))