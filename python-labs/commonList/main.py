import random

'''
This lab is solving the following problem:
    Code a solution that takes two lists and compares all elements. All common elements should be added to a new list and printed out in terminal.
'''

num_in_list = int(input("Enter a number between 10 and 20 ===> "))

list_1 = [random.randint(1, num_in_list) for i in range(num_in_list)]

list_2 = [random.randint(1, num_in_list) for i in range(num_in_list)]

print(f'List 1 : {list_1}\nList 2: {list_2}')

common_elems = []

for element in list_1:
    if element in list_2:
        common_elems.append(element)


list_1.sort()
list_2.sort()
print(
    f'List 1 : {list_1}\nList 2 : {list_2}\n\nCommon Elements : {common_elems}')
