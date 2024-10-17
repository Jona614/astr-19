# Define a class that allows you to create a sheep
class Sheep():
    # Instantiate the state variables that relate to the physical parts of a sheep
    def __init__(self, front_limbs_length, hind_limbs_length, number_of_eyes, has_tail, is_furry):
        self.front_limbs_length = front_limbs_length
        self.hind_limbs_length = hind_limbs_length
        self.number_of_eyes = number_of_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry
    
    # Prints the information of the created sheep's physical parts
    def description(self):
        # If the Boolean passed in for has_tail and is_furry are either True or false, a new variable will hold a certain string
        has_tail_word = 'does' if self.has_tail is True else 'does not'
        is_furry_word = 'is' if self.is_furry is True else 'is not'

        print(f'''You have created a sheep.
Its front limbs has a length of {self.front_limbs_length} centimeters.
Its hind limbs has a length of {self.hind_limbs_length} centimeters.
It has a number of {self.number_of_eyes} eyes.
It {has_tail_word} have a tail.
It {is_furry_word} furry.
''')

def main():
    # Instantiate the sheep object and pass in certain arguments, which are information of the sheep's physical parts
    my_sheep = Sheep(12, 14, 2, True, True)
    # Call the sheep object's method, which will print the sheep's description
    my_sheep.description()

# Calls the main function if the program that is being runned is this exact program
if __name__ == '__main__':
    main()