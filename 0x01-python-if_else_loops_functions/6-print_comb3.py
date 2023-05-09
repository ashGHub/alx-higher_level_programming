#!/usr/bin/python3
for i in range(1, 99):
    if (i == 89):
        print("89")
    elif ((((i % 10) * 10) + (i // 10)) > i):
        print("{:02d}".format(i), end=', ')
