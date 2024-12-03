import numpy as np


def main():
    """Calculate the diff & similarity score between 2 lists after sorting them in descening order"""
    reports = load_input();
    valid_reports = count_valid_reports(reports)
    print('valid report count is ' +str(valid_reports))

def load_input():
    with open('day2_input.txt') as file:
        return np.array([load_line(line.strip()) for line in file.readlines()], dtype=object)


def load_line(line):
    return [int(part) for part in line.split(' ')]

def count_valid_reports(reports):
    valid_reports = 0
    for i in range(len(reports)):
        report = reports[i]
        if(is_valid_report(report, should_try_again=True, index=i)):
            valid_reports+=1

    return valid_reports


def is_valid_report(report, should_try_again=False, index=0):
    is_ascending = None
    is_descending = None
    is_valid = True
    for i in range(1, len(report)):
        # check if it stops ascending (or just started ascending)
        is_bigger = report[i]>report[i-1]
        if(is_bigger):
            if(is_descending is True):
                is_valid = False
            else:
                is_ascending = True
                is_descending = False

        # check if it stops descending (or just started descending)
        is_smaller = report[i]<report[i-1]
        if(is_smaller):
            if(is_ascending is True):
                is_valid = False
            else:
                is_descending = True
                is_ascending = False
        
        # check if it's equal to the previous value
        is_equal = report[i]==report[i-1]
        is_very_different = abs(report[i]-report[i-1])>3

        if(is_equal or is_very_different):
            is_valid = False

    if(is_valid is False and should_try_again):
        return is_valid_through_dampening(report)

    return is_valid

def is_valid_through_dampening(report):
    is_dampened_to_valid_report = False
    for dampen_index in range(len(report)):
        dampened_list = np.array([report[j] for j in range(len(report)) if j != dampen_index])
        retry_is_valid = is_valid_report(dampened_list, should_try_again=False)
        if(retry_is_valid is True):
            is_dampened_to_valid_report = True
            break;
    return is_dampened_to_valid_report


if __name__ == "__main__":
    main()
