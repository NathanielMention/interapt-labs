from statistics import mean

# Write a program that accepts numeric inputs and adds them to a set.
# Hit <enter> when done

user_string = input(
    f'Enter numbers to add into your set, hit <enter> when done: ')
input_str = user_string.split()
print(input_str)

input_ints = [int(i) for i in input_str]
print(input_ints)

user_set = set(input_ints)
print(user_set)

print('\n')
# After making entries, print the largest, smallest, sum, and average of all elements

print(f'This is the largest num of your set:\t{max(user_set)}')
print(f'This is the smallest num of your set:\t{min(user_set)}')
print(f'This is the sum of all numbers in your set:\t{sum(user_set)}')
print(f'This is the average number of all nums in your set:\t{mean(user_set)}')
