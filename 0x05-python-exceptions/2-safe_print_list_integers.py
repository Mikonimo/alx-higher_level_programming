#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print("{:d}", end="")
            count += 1
    except ValueError:
        pass
    except TypeError:
        pass
    except IndexError:
        pass
    print()
    return count
