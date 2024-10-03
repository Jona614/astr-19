# This function adds two numbers together and returns the sum
def addition(x, y):
    return x + y

# This function subtracts two numbers together and returns the difference
def subtraction(x, y):
    return x - y

# This function multiplies two numbers together and returns the product
def multiplication(x, y):
    return x * y

# This function returns the data type of the number passed in
def type_num(num):
    return type(num)


def main():
    # Three variables that consist of
    # the sum of two decimals, the difference of two integers, and the product of a decimal and integer respectively
    add_float_nums = addition(542.736, 3412.265)
    subtract_ints = subtraction(45, 32)
    multiply_float_and_num = multiplication(2453.432, 5243)

    # Three variables that consist of the data types of the sum, difference, and product respectively
    add_float_nums_type = type_num(add_float_nums)
    subtract_ints_type = type_num(subtract_ints)
    multiply_float_and_num_type = type_num(multiply_float_and_num)

    # Prints all the variables
    print(f'''Your sum of two decimals: {add_float_nums}\tThe data type of your sum: {add_float_nums_type}
Your difference of two integers: {subtract_ints}\tThe data type of your difference: {subtract_ints_type}
Your product of one decimal and one integer: {multiply_float_and_num}\tThe data type of your product: {multiply_float_and_num_type}''')

# Calls the main function if the program that is being runned is this exact program
if __name__ == '__main__':
    main()