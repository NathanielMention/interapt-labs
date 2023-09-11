#!/usr/bin/env python3

# Part 1: Write a number-guessing game
# Keep track of number of guesses - stop when # guesses = num_to_guess
# for now.....
biggest_num = 100
num_to_guess = 45

num_found = False
num_guesses = 0
max_num_guesses = 5
while input("Wanna play the number guessing game? (y or n) ==> ").upper() == "Y":
    while (not num_found and num_guesses < max_num_guesses):
        # No exception checking here - better enter a number!
        my_guess = int(
            input(f"Enter a number between 1 and {biggest_num} ==> "))
        # Check if number really between 0 and the big_number
        if not (0 < my_guess < biggest_num):
            print(f"{my_guess} is an invalid entry... try again\n")
            continue
        # If we get here, the number entered is valid
        num_guesses += 1
        if num_found := my_guess == num_to_guess:
            print(f'You found the number {num_to_guess}! '
                  f'And it took you {num_guesses} guesses to find it')
        else:
            # Tell player guess is too low...too high and number of guesses left
            print(
                f"{my_guess} is too {('high' if my_guess > num_to_guess else 'low')}")
            num_left = "no" if max_num_guesses == num_guesses \
                else (max_num_guesses - num_guesses)
            print(f'You have {num_left} guesses left.\n')


# Part 2: Write a menu for a CRUD application

user_wants_to_continue = True
while user_wants_to_continue:
    option = input(
        'Enter: \n\tC to create, \n\tR to read, \n\tU to update, \n\tD to delete or \n\tQ to quit ==> ').upper()
    # Call applicable routine based on user input
    if option == "C":
        print("Calling CREATE routine.....")
    elif option == "R":
        print("Calling READ routine.....")
    elif option == "U":
        print("Calling UPDATE routine.....")
    elif option == "D":
        print("Calling DELETE routine.....")
    elif option == "Q":
        print("Exiting program")
        user_wants_to_continue = False
    else:
        print(f"Your entry {option} is invalid - try again")
