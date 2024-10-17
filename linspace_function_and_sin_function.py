# Import the numpy module and assign it to an alias
import numpy as np

# A function that can take in two arguments, which should be numbers
def tables(start, end):
    # Create an array that consists of 1000 evenly-spaced elements within the range between 'start' and 'end'
    x = np.linspace(start, end, 1000)
    # Change the shape of the array to having 1000 rows, and 1 column
    x = x.reshape(1000, 1)
    # Create another array that has the same dimensions as the x array; the values in this array are sin(x_value)
    sine = np.sin(x)
    # Return the x and sine arrays as a tuple
    return x, sine
    
def main():
    # Assign the arrays into each variable respectively
    x, sine = tables(0, 2*np.pi)

    # Iterate over all the x and sine values.
    # The arrays will be packed into a tuple, the values will be rounded, and they will be printed
    for x, y in zip(x, sine):
        round_x = round(float(x), 8)
        round_sine = round(float(y), 8)
        print(f'x: {round_x}, sin(x): {round_sine}')

# Calls the main function if the program that is being runned is this exact program
if __name__ == '__main__':
    main()