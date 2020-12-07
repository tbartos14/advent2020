'''
Day 6 Pt 1
Tim Bartos 2020
Counting letters across groups
'''

from typing import IO, List, Set, Dict

input_file: IO = open("input.txt")  # open
entire_file: str = input_file.read()  # interpret
entire_file = entire_file[:-1]  # remove end
split_str: List[str] = entire_file.split("\n\n")  # split

split_str = list(map(lambda x: x.replace("\n", ""), split_str))
letters = list(map(lambda x: len(set(x)), split_str))

print(sum(letters))