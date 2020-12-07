'''
Day 6 Pt 2
Tim Bartos 2020
Counting letters within and across groups
'''

from typing import IO, List, Set, Dict

input_file: IO = open("input.txt")  # open
entire_file: str = input_file.read()  # interpret
entire_file = entire_file[:-1]  # remove end
split_str: List[str] = entire_file.split("\n\n")  # split

split_str = list(map(lambda x: x.split("\n"), split_str))
letters = list(map(lambda x: list(map(lambda y: set(y), x)), split_str))
letters = list(map(lambda x: len(set.intersection(*x)), letters))

print(sum(letters))