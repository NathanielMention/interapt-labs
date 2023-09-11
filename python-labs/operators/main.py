#!/usr/bin/env python3

# Part 1: Arithmetic operators

an_int = 100
another_int = 200
a_float = 2.71828
another_float = 3.14159

print(f'{an_int} times {a_float} = {an_int * a_float}')
print(f'{an_int} divided by {a_float} = {an_int / a_float}')
print(f'{a_float} raised to the power of {another_float} '
      f'to 6 decimals is {a_float ** another_float:.6f}')
print(f'{an_int} plus {another_int} THEN multiplied by {a_float} '
      f'is {(an_int + another_int) * a_float }')
print('{an_int} plus {another_int} THEN divided by {a_float} plus '
      '{another_float} is {(an_int+another_int)/(a_float+another_float)} ')
print(f'{an_int} divided by {a_float} plus {another_int} divided by {another_float} '
      f'is {an_int/a_float + another_int/another_float}')
print()
# Part 2: Compare and logical operators
# Use the same values as in part 1
print(f'Is {an_int} less than {another_int}?  {an_int < another_int }')
print(f'Is {an_int} greater than {a_float} OR {another_float} equal to {another_int}? '
      f'{an_int > a_float or another_float == another_int}')
print(f'Is {an_int} cubed greater than {another_int} squared? '
      f'{an_int ** 3 > another_int ** 2 }')
print(f'Is true greater than false? {True > False}')
print()
# Membership operators
a_string = "abcdef"
print(f'The letter "f" in "{a_string}" ? {"f" in a_string} ')
print(f'The letter "K" is not in "{a_string}" ? {"K" not in a_string} ')
print()
# Identity operators
num1 = 100
num2 = 100.0
print(f'{num1} equals {num2} ? {num1 == num2 }')
print(f'{num1} is the same object as {num2} ? {num1 is num2}')
print()
# Part 2: Convert from Celsios to Fahrenheit
# No error checking done here for invalid inputs
cels_temp = float(input("Enter a Celsuis temperature ==> "))
print(f'Fahrenheit equivalent is { ( ( 9 * cels_temp) / 5 ) + 32}')
