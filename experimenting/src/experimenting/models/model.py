import numpy as np
import matplotlib.pyplot as plt
from time import time
import math


def factorial_firstmeth(n):
    factorial = int(1)
    for number in range(1, n + 1):
        factorial = int(factorial * number)
    return factorial


def factorial_secondmeth(n):
    if n == 1:
        factorial = 1
    else:
        factorial = factorial_secondmeth(n=n - 1) * n
    return factorial


if __name__ == "__main__":
    n = 5000
    begin = time()
    factorial = factorial_firstmeth(n)

    end = time()
    print(f"time taken:{end-begin} s, answer = {factorial}")
    begin = time()
    factorial = factorial_secondmeth(n)
    end = time()
    print(f"time taken:{end-begin} s, answer = {factorial}")
    begin = time()
    factorial = math.factorial(n)
    end = time()
    print(f"time taken:{end-begin} s, answer = {factorial}")
