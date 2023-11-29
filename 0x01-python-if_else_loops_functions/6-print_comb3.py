#!/usr/bin/python3

for n in range(0, 10):
    for n in range(digit1 + 1, 10):
        if digit1 == 8 and n == 9:
            print("{}{}".format(digit1, n))
        else:
            print("{}{}".format(digit1, n), end=", ")
