#!/usr/bin/python3
import sys
# Make a program that accepts two numbers from the command line, an integer
# and a base.  Convert the first number to a string in the given base, then
# output the string.  Base may range from 2 to 16.  You may use atoi(), but
# you may not use %d,%x or %o in printf or sprintf to directly print any
# numbers.
# 
# Example input/output:
# ./p2 101 2
# 1100101
# ./p2 65535 16
# FFFF
letters = "ABCDEF"

if __name__ == "__main__":
    args = sys.argv
    if len(args)<3:
        print("Usage: python p2.py [number] [base]")
        sys.exit(0)
    num = int(args[1])
    base = int(args[2])
    string = ""

    while num>0:
        digit = num%base
        if digit>9:
            digit = letters[digit-10]
        string = str(digit) + string
        num = num//base
    print(string)
