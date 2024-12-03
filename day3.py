import regex as re


def main():
    '''using https://regex101.com/'''

    multiplication_pattern = "mul\([0-9]{1,3},[0-9]{1,3}\)"
    with open('day3_input.txt') as file:
        text = file.read()
    multiplications = re.findall(multiplication_pattern, text)
    sum_of_multiplications = get_sum_of_multiplications_functions(multiplications)
    print(sum_of_multiplications)


def get_sum_of_multiplications_functions(multiplications):
    sum = 0
    numbers_in_function_pattern = "[0-9]{1,3}"
    for multiplication in multiplications:
        numbers = re.findall(numbers_in_function_pattern, multiplication)
        multiplication_result = int(numbers[0])*int(numbers[1])
        sum += multiplication_result
    return sum


if __name__ == "__main__":
    main()
