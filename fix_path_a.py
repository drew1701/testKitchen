#!/usr/bin/env python3
"""
Drew Patrick
testKitchen : fix_path_a.py
Task:
 Write a program that switches rx_PATH between local dir and
 required path on hills '/users/abrick/resources/filename.txt'
"""
# _a is first working version

BAD_PATH = r"badpath.txt"
# BAD_PATH = r"other/badpath1.txt"

with open(BAD_PATH) as r:
    text = r.read().replace('rx_PATH = "badpath.txt"',
                            'rx_PATH = "other/badpath.txt"')
with open(BAD_PATH, "w") as w:
    w.write(text)
