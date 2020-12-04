'''
Day 3 Pt 1
Tim Bartos 2020
Find path for a sled
'''

from typing import IO, List

input_file: IO = open("input.txt")  # open
split_str: List[str] = input_file.readlines()  # interpret
split_str = list(map(lambda x: x.strip(), split_str))  # strip

slope = 3
width = len(split_str[0])

trees: int = 0
for val in range(len(split_str)):
    # print(f"{val},{slope * val}: {split_str[val][(slope * val) % width]}")
    if split_str[val][(slope * val) % width] == "#":
        trees += 1

print(trees)