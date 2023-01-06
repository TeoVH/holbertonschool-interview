#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text
editor can execute only two operations in this file: Copy
All and Paste. Given a number n, write a method that
calculates the fewest number of operations needed to result
in exactly n H characters in the file.
- Prototype: def minOperations(n)
- Returns an integer
- If n is impossible to achieve, return 0
"""


def countProcess(num):
    """ Return list of process until n H """
    counter = 1
    p_list = []
    val = num
    while val != 1:
        counter += 1
        if val % counter == 0:
            while (val % counter == 0 and val != 1):
                val /= counter
                p_list.append(counter)

    return p_list


def minOperations(n):
    """ Return sum of process until n H """
    if n < 2 or type(n) is not int:
        return 0
    values = countProcess(n)
    return sum(values)
