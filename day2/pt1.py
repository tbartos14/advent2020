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
    valid_range = range(int(valid_range.split("-")[0]),
                        int(valid_range.split("-")[1])+1)
    if password.count(char) in valid_range:
        valid += 1

print(valid)