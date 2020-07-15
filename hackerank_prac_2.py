#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    value1 = 0
    value2 = 0
    count1 = 0
    count2 = 0
    for i in apples:
        value1 = a + i
        if value1 >= s and value1<= t:
            count1+=1
    print(count1)
    for j in oranges:
        value2 = b + j
        if value2 <= t and value2>= s:
            count2+=1
    print(count2)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
