#!/usr/bin/env python3

from string import punctuation
import os
mba = BankAccount("d12", "Lou", 12345.67)

try:
    mba.makeDeposit(123_456_789_111_222)
except ValueError as ve:
    # whatevs

v = 2.718 * 3.141549


def makeDeposit(self, dep_amt):
    if 0 < dep_amt < 100_000:
        raise ValueError(f"The deposit amount {dep_amt} is invalid")

    self._balance += dep_amt


# PART 2 with dictionary (OPTIONAL):
# There may be duplicate lines - we need to get rid of the dupes!
# Get a DICT of all sentences that match the criteria.
# The line is the key (that takes care of the duplicates)
# The long word is the value
with open('smedleybutler.txt') as sb:
    smed_dict = {a_line: a_word for a_line in sb
                 for a_word in a_line.split(" ") if len(a_word) > 9}
# Write to file
with open('bigwords.txt', 'w') as bw:
    bw.writelines([f'Word: {smed_dict[ line_key ]}  Line: {line_key} '
                   for line_key in smed_dict])

os.system('type bigwords.txt')
exit()
# Part 2: Read smedleybutler.txt, copy all lines containing at least
# one word > 9 characters to another file named bigwords.txt

# Get a SET of all sentences that match the criteria.
# There may be duplicate lines - we need to get rid of the dupes!
with open('smedleybutler.txt') as sb:
    smed_set = {a_line for a_line in sb
                for a_word in a_line.split(" ") if len(a_word) > 9}
# Write to file
with open('bigwords.txt', 'w') as bw:
    bw.writelines(smed_set)

os.system('type bigwords.txt')


exit()
# Part 1: Read abespeech.txt, strip newline, print out line numbers and the line backwards
with open('abespeech.txt') as abe:
    for line_idx, a_line in enumerate(abe, 1):
        rev_line = list(a_line[: -1])
        rev_line.reverse()
        print(f'{line_idx}\t {"".join(rev_line)}')
exit()
