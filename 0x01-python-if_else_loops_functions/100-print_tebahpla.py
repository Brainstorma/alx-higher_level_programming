#!/usr/bin/python3
for val in range(ord('z'), ord('A')-1, -1):
    if val % 2 == 0:
        print("{:c}".format(val), end="")
    else:
        print("{:c}".format(val-32), end="")
