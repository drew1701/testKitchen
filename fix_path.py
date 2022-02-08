#!/usr/bin/env python3
"""
Drew Patrick
testKitchen : fix_path.py
Task:
 Write a program that switches rx_PATH between local dir and
 required path on hills '/users/abrick/resources/filename.txt'
"""

import re

BAD_PATH = r"badpath.txt"
# BAD_PATH = r"other/badpath1.txt"

with open(BAD_PATH) as reader:
    for line in reader:
        print(line, end='')

print('\n\nand now the reader object itself\n')
print(reader)