#!/usr/bin/env python3
'''
Use the module strings
Just copy the main function from the mmodule and
put tht code here if you like....
'''
from strings import string_length, make_upper_case, make_lower_case, make_title_case

a_string = "Mary had a little lamb"

print(f'Calling stringstuff functions from my program {__file__}')

print(f'Original string: {a_string}')
print(f'Upper case: {make_upper_case(a_string)}')
print(f'Lower case: {make_lower_case(a_string)}')
print(f'Title case: {make_title_case(a_string)}')
print(f'Number of characters: {string_length(a_string)}')
