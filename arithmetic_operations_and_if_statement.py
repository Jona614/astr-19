# This function returns the result of this operation: passed-in number to the power of 3 added by 8
def f(x):
    return x ** 3 + 8

def main():
    # Prints the result of the complex operation; the passed-in number will be 9
    result = f(9)
    print(result)

    # If the result is greater than 27, then the string 'YAY!' will be printed into the terminal
    if result > 27:
        print('YAY!')

# Calls the main function if the program that is being runned is this exact program
if __name__ == '__main__':
    main()