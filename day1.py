left_list = [];
right_list = [];


def main():
    """Calculate the diff & similarity score between 2 lists after sorting them in descening order"""
    load_input();
    left_list.sort()
    right_list.sort()
    calculate_difference()
    calculate_similarity_score()

def calculate_similarity_score():
    score = 0
    for i in range(len(left_list)):
        current_left_number = left_list[i]
        occurences_in_right = right_list.count(current_left_number)
        current_sim_score = current_left_number * occurences_in_right
        score += current_sim_score
    print('the total sim score is '+str(score))


def calculate_difference():
    diff = 0
    for i in range(len(left_list)):
        diff+=abs(left_list[i]-right_list[i])
    print('the total diff is '+str(diff))

def load_input():
    with open('day1_input.txt') as file:
        [load_line(line.strip()) for line in file.readlines()]

def load_line(line):
    parts = line.split('   ');
    left_list.append(int(parts[0]))
    right_list.append(int(parts[1]))


if __name__ == "__main__":
    main()
