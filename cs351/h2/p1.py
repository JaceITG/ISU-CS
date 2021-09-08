#!/usr/bin/python3

# In this assignment you may not use atoi or strtol() or any other libc
# function to convert a string to a number.
# 
# Make a program that implements an atoi like function, say ascii2int()
# that takes a string and an integer base to convert the string to a number
# of the given base, i.e. ascii2int("101",2) would convert 101 as a binary
# number where ascii2int("101", 10) would convert 101 as a decimal number.
# 
# Your function should handle bases from 2 though 16 (it does not need to
# error check this input.)  It should stop processing the string if the
# character is not a valid digit in the given base.
# 
# The program should accept two strings, one the number to be converted
# and a second base (always specified in decimal.)  Use the ascii2int()
# function to covert both numbers and print the first number after
# conversion.
# 
# Example input/output:
# ./p1.py 101 2
# 5
# ./p1.py 101 10
# 101
# ./p1.py 101 16
# 257

