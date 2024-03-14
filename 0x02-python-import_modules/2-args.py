#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv) - 1
    if ac == 0:
        print("0 arguments.")
    elif ac == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(ac))
    for n in range(1, ac + 1):
        print("{}: {}".format(n, argv[n]))
    