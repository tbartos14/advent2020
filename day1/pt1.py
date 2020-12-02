'''
Day 1 Pt 1
Tim Bartos 2020
Two entries that sum to 2020, find the product.
'''

from typing import IO, List
from itertools import combinations

input_file: IO = open("input.txt")  # open
split_str: List[str] = input_file.readlines()  # interpret
split_str = list(map(lambda x: x.strip(), split_str))  # strip
vals: List[int] = list(map(lambda x: int(x), split_str))  # type conversion

# sort the values, to make finding the matching pair easy
vals.sort()
for pair in combinations(vals, 2):
    print(f"Pair {pair[0]} and {pair[1]}")
    if (pair[0] + pair[1]) == 2020:
        print(f"Matching pair {pair[0]} and {pair[1]}, gives product {pair[0] * pair[1]}")
        break