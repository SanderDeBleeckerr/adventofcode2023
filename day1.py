left_list = [];
right_list = [];


def main():
    """Calculate the diff between 2 lists after sorting them in descening order"""
    load_input();
    left_list.sort()
    right_list.sort()
    diff = 0
    for i in range(len(left_list)):
        diff+=abs(left_list[i]-right_list[i])
    print(diff)

def load_input():
    with open('day1_input.txt') as file:
        [load_line(line.strip()) for line in file.readlines()]

def load_line(line):
    parts = line.split('   ');
    left_list.append(int(parts[0]))
    right_list.append(int(parts[1]))


if __name__ == "__main__":
    main()
