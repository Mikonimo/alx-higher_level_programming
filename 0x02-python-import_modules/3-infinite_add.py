#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    ac = len(argv) - 1
    for n in range(ac):
        result += int(argv[n + 1])
    print("{:d}".format(result))
