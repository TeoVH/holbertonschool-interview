#!/usr/bin/python3
"""
Exercise:
You have n number of locked boxes in front of you. Each box is
numbered sequentially from 0 to n - 1 and each box may contain
keys to the other boxes.
Write a method that determines if all the boxes can be opened.

Exercise Information:
- (boxes) is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    Function to know if boxes can be opened
    """
    keys = [0]
    for key in keys:
        box = boxes[key]
        for key_in_box in box:
            if key_in_box not in keys and key_in_box < len(boxes):
                keys.append(key_in_box)
    if len(keys) == len(boxes):
        return True
    return False