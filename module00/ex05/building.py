import string

def main(*args):
    import sys

    print(len(sys.argv))
    if len(sys.argv) > 2:
        print("Error: Please provide exactly one string argument.")
        sys.exit(1)
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] == "None"):
        print('What is the text to count ?')
        print(end='')
        input_string = sys.stdin.readline()
    else:
        input_string = sys.argv[1]
    
    char_sums = calculate_char_sums(input_string)

    print(f'The text contains {char_sums["characters"]} characters:')
    for category, count in char_sums.items():
        print(f'{count} {category} ')
def calculate_char_sums(input_string):
    """
    Calculate the sums of upper-case characters, lower-case characters,
    punctuation characters, digits, and spaces in the input string.

    Args:
        input_string (str): The input string.

    Returns:
        dict: A dictionary containing the sums of each category.
    """
    char_sums = {
        'characters': 0,
        'upper leters': 0,
        'lower letters': 0,
        'punctuantion marks': 0,
        'spaces': 0,
        'digits': 0
    }

    for char in input_string:
        char_sums['characters'] += 1
        if char.isupper():
            char_sums['upper leters'] += 1
        elif char.islower():
            char_sums['lower letters'] += 1
        elif char in string.punctuation:
            char_sums['punctuantion marks'] += 1
        elif char.isdigit():
            char_sums['digits'] += 1
        elif char.isspace():
            char_sums['spaces'] += 1
    return char_sums


if __name__ == "__main__":
    main()
