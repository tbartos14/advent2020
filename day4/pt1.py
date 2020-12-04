'''
Day 4 Pt 1
Tim Bartos 2020
Validating python strings as passports
'''

from typing import IO, List, Set, Dict

input_file: IO = open("input.txt")  # open
entire_file: str = input_file.read()  # interpret
entire_file = entire_file[:-1]  # remove end
split_str: List[str] = entire_file.split("\n\n")  # split

valid_passports: int = 0
needed_fields: Set[str] = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

print(len(split_str))
for passport in split_str:
    flattened = " ".join(passport.split("\n"))
    kv_pair = list(map(lambda x: x.split(":"), flattened.split(" ")))
    passport_dict: Dict[str, str] = dict(kv_pair)
    if len(needed_fields.intersection(set(passport_dict.keys()))) == 7:
        valid_passports += 1

print(f"Number of valid passports: {valid_passports}")