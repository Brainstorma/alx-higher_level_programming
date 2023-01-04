#!/usr/bin/python3
for ran in range(0, 10):
    for ang in range(ran + 1, 10):
        if ran == 8 and ang == 9:
            print("{}{}".format(ran, ang))
        else:
            print("{}{}".format(ran, ang), end=", ")
