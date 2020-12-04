'''
Day 3 Pt 2
Tim Bartos 2020
Find path for a sled, multiple times
'''

from typing import IO, List
from functools import reduce
import sys


input_file: IO = open("input.txt")  # open
split_str: List[str] = input_file.readlines()  # interpret
split_str = list(map(lambda x: x.strip(), split_str))  # strip

tree_goal: List[int] = []
for slope in [1,3,5,7,0.5]:
    width = len(split_str[0])

    trees: int = 0

    for val in range(len(split_str)):
        # print(f"{val},{slope * val}: {split_str[val][(slope * val) % width]}")
        if abs(int(slope*val)-(slope*val)) < sys.float_info.epsilon:
            if split_str[val][(int(slope * val)) % width] == "#":
                trees += 1

    print(trees)
    tree_goal.append(trees)

print(reduce(lambda x, y: x * y, tree_goal))
