#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ln = len(sys.argv) - 1
    if (ln == 0):
        print("0 arguments.")
        sys.exit(0)
    if (ln == 1):
        print("{:d} argument:".format(ln))
    else:
        print("{:d} arguments:".format(ln))
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
