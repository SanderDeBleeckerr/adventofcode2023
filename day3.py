import regex as re


def main():
    '''using https://regex101.com/'''

    pattern = "mul\([0-9]{1,3},[0-9]{1,3}\)"
    text = "mul(123,1)ezzefzefz"
    matches = re.findall(pattern, text)
    print(matches)


if __name__ == "__main__":
    main()
