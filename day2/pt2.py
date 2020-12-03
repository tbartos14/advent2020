'''
Day 2 Pt 1
Tim Bartos 2020
Find valid passwords in given file, based on criteria
'''

from typing import IO, List

input_file: IO = open("input.txt")  # open
split_str: List[str] = input_file.readlines()  # interpret
split_str = list(map(lambda x: x.strip(), split_str))  # strip

# find the rule and password
rule_and_pass = list(map(lambda x: x.split(": "), split_str))

valid: int = 0
for rp in rule_and_pass:
    rule, password = rp
    valid_range, char = rule.split(" ")
    lval, rval = list(map(lambda x: int(x), valid_range.split("-")))
    a: bool = password[lval-1] == char
    b: bool = password[rval-1] == char
    if (a and not b) or (not a and b):
        valid += 1

print(valid)