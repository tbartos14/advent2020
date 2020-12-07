'''
Day 5 Pt 2
Tim Bartos 2020
Airplanes oh my! This time finding missing index
'''

from typing import IO, List, Set, Dict
import numpy as np

input_file: IO = open("input.txt")  # open
entire_file: str = input_file.read()  # interpret
entire_file = entire_file[:-1]  # remove end
split_str: List[str] = entire_file.split("\n")  # split

ids: np.ndarray = np.array(sorted([int(val[:7].replace("F", "0").replace("B", "1"),2) * 8 + \
                  int(val[7:].replace("L", "0").replace("R", "1"),2)
                  for val in split_str]))
missing_index: int = ids[:-1][np.diff(ids) != 1] + 1

print(f"Missing index is {missing_index}")