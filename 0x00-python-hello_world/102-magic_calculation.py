#!/usr/bin/python3
def magic_calculation(a, b):
    return a ** b + 98
# Disassembly of magic_calculation:
#  2           0 LOAD_FAST                0 (a)
#              2 LOAD_FAST                1 (b)
#              4 BINARY_POWER
#              6 LOAD_CONST               1 (98)
#              8 BINARY_ADD
#             10 RETURN_VALUE
