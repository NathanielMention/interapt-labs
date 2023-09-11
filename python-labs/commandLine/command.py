# part 1

import sys

my_name = input("Enter your name ==> ")

# Check if the user entered a name
if my_name:
    print(f"Hello, {my_name}!")
else:
    print("Hello, World!")


# part 2

# Check if the number of command-line arguments is correct (2)
if len(sys.argv) != 3:
    print("Usage: python program.py <number1> <number2>")
else:
    # Attempt to convert the command-line arguments to numbers
    try:
        number1 = float(sys.argv[1])
        number2 = float(sys.argv[2])

        # Calculate the sum
        result = number1 + number2

        # Print the result using an f-string
        print(f"The sum of {number1} and {number2} is {result}")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
