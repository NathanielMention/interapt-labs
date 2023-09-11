#!/usr/bin/env python3

# Part 1: Print out a big A without using hand-entered spaces
# Use formatting statements instead
letter_a = "A"
three_spaces = "   "
print(f'{letter_a: ^38}')
print(f'{letter_a: >17}{three_spaces}{letter_a:<17}')
print(f'{letter_a: >16}', end="")
print(f'{letter_a}{letter_a}{letter_a}{letter_a}{letter_a}{letter_a:<15}')
print(f'{letter_a: >15}{three_spaces:>7}{letter_a:<15}')
print(f'{letter_a: >14}{three_spaces:>9}{letter_a:<14}')

print()
# Part 2: Print out the following expressions:
num1 = 100
num2 = 3.14159
print(f'{num1} multiplied by {num2} = {num1 * num2:.5f}')
print(f'The type of {num1} is {type( num1 ) }')
print(f'The type of {num2} is {type( num2 ) }')
print(f'The unique object identifier of {num1} is {id( num1 ) }')
print(f'The unique object identifier of {num2} is {id( num2 ) }')
print()
# Part 3: Are strings the same?
string1 = "Hello"
string2 = "Hello"
# Verify these are the same object...Are these strings the same?
print(f'On assignment: {id(string1) = }\t\t{id(string2) = } ')
string1 = string1 + " There"
string2 = string2 + " There"
# How about now? Are these the same string now?
# Are they the same string as their previous values when defined?
print(f'After concatentation: {id(string1) = }\t\t{id(string2) = } ')
# Are these numbers the same?
num1 = 10
num2 = 10.0
print(f'On assignment: {id(num1) = }\t\t{id(num2) = } ')
# Verify that Python assigns a different object reference to
# num1 and num2 than it had before the arithmetic
num1 = num1 + 100
num2 = num2 - 5
print(f'After arithmetic : {id(num1) = }\t\t{id(num2) = } ')
