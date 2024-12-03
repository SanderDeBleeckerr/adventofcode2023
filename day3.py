import regex as re


def main():
    '''calculates a sum via instructions read from a gibberish file'''

    # regex patterns tested using https://regex101.com/
    multiplication_pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don\'t\(\)"
    parsable_functions_pattern = f'{multiplication_pattern}|{do_pattern}|{dont_pattern}'

    with open('day3_input.txt') as file:
        text = file.read()
    functions = re.findall(parsable_functions_pattern, text)
    sum_of_multiplications = get_sum_of_multiplications_functions(functions, multiplication_pattern, do_pattern, dont_pattern)
    print(sum_of_multiplications)


def get_sum_of_multiplications_functions(functions, multiplication_pattern, do_pattern, dont_pattern):
    sum = 0
    numbers_in_function_pattern = "[0-9]{1,3}"
    may_parse_multiplication = True
    for parsable_function in functions:
        if re.match(do_pattern, parsable_function):
            may_parse_multiplication = True
            continue
        elif re.match(dont_pattern, parsable_function):
            may_parse_multiplication = False
            continue
        elif re.match(multiplication_pattern, parsable_function) and may_parse_multiplication:
            numbers = re.findall(numbers_in_function_pattern, parsable_function)
            multiplication_result = int(numbers[0])*int(numbers[1])
            sum += multiplication_result
    return sum


if __name__ == "__main__":
    main()
