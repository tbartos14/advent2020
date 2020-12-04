'''
Day 4 Pt 2
Tim Bartos 2020
Validating python strings as passports
(With tedious regex for no good reason)
'''

from typing import IO, List, Set, Dict
import re

input_file: IO = open("input.txt")  # open
entire_file: str = input_file.read()  # interpret
entire_file = entire_file[:-1]  # remove end
split_str: List[str] = entire_file.split("\n\n")  # split

valid_passports: int = 0
needed_fields: Set[str] = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
re_validation: Dict[str, str] = {
    "byr": "^(19[2-9][0-9]|200[0-2])$",  # 1920-2002
    "iyr": "^(201[0-9]|2020)$",  # 2010-2020
    "eyr": "^(202[0-9]|2030)$",  # 2020-2030
    "hgt": "^(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)$",  # 150-193cm, or 59-76in
    "hcl": "^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$",  # valid hex color
    "ecl": "^(amb|blu|brn|gry|grn|hzl|oth)$",  # in set amb, blu, brn, gry, grn, hzl, oth
    "pid": "^\\d{9}$",  # 9 digit number
}

print(len(split_str))
for passport in split_str:
    flattened = " ".join(passport.split("\n"))
    kv_pair = list(map(lambda x: x.split(":"), flattened.split(" ")))
    # print(kv_pair)
    passport_dict = dict(kv_pair)
    if len(needed_fields.intersection(set(passport_dict.keys()))) == 7:
        if all([bool(re.match(value, passport_dict[key])) for key, value in re_validation.items()]):
            valid_passports += 1
            if "cid" in passport_dict.keys():
                passport_dict.pop("cid")
            print(sorted(passport_dict.items()))
            print([bool(re.match(value, passport_dict[key])) for key, value in re_validation.items()])
        # else:
            # print(passport_dict)
print(f"Number of valid passports: {valid_passports}")