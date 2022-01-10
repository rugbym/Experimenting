import numpy as np
import matplotlib.pyplot as plt
from time import time
from statistics import mean, stdev
import math
from numpy import prod
from functools import reduce
from operator import mul


def timetester(func, repeats: int, n: int):
    timelist = list()
    for _ in range(repeats):
        begin = time()
        faculteit = func(n)
        end = time()
        timelist.append(end - begin)
    return mean(timelist), stdev(timelist) / repeats


def factorial_firstmeth(n):
    factorial = int(1)
    for number in range(1, n + 1):
        factorial = int(factorial * number)
    return factorial


def factorial_np(n):
    """Fastest way to calculate factorials"""
    factorial = prod(range(1, n + 1))
    return factorial


def factorial_mul(n):
    factorial = reduce(mul, range(1, n + 1))
    return factorial


def factorial_secondmeth(n):
    # function has a recursion limit. returns error after a number of recursion
    # basic limit is 998 recursions
    # set to desired number using:
    # import sys
    # sys.setrecursionlimit(1500)
    # also recursion is way slower
    if n == 1:
        factorial = 1
    else:
        factorial = factorial_secondmeth(n=n - 1) * n
    return factorial


if __name__ == "__main__":
    n = 50000
    repeats = 10
    avg, std = timetester(factorial_firstmeth, repeats=repeats, n=n)
    print(f"average time taken: {avg} \u00B1 {std} s")
    # avg, std = timetester(factorial_secondmeth, repeats=repeats, n=n)
    # print(f"average time taken: {avg} \u00B1 {std} s")
    avg, std = timetester(math.factorial, repeats=repeats, n=n)
    print(f"average time taken: {avg} \u00B1 {std} s")
    # fastest way to calculate factorials
    avg, std = timetester(factorial_np, repeats=repeats, n=n)
    print(f"average time taken: {avg} \u00B1 {std} s")
    avg, std = timetester(factorial_mul, repeats=repeats, n=n)
    print(f"average time taken: {avg} \u00B1 {std} s")
