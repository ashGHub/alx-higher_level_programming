#!/usr/bin/python3
for i in range(122, 96, -1):
    j = i
    if (j % 2 != 0):
        j = i - 32
    print("{:c}".format(j), end='')
