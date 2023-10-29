import sys

def main():
    program = sys.argv
    if len(program) != 2 :
        print(AssertionError('more than one argument is provided'))
        return
    try:
        arg = int(program[1])
    except ValueError:
        print(AssertionError('argument is not an integer'))
        return
    if arg % 2 == 0:
        return print("I'm Even.")
    else:
        return print("I'm Odd.")


if __name__ == "__main__":
    main()