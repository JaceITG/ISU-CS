#!/usr/bin/env python3

import sys

VERSION = '0.0.1'

#get all arguments passed
args = sys.argv[1:]

#ensure args have been passed
if len(args) == 0:
    print("You must provide arguments to this program.", file=sys.stderr)
    exit(1)

#check for ver
if "-v" in args or "--version" in args:
    print(VERSION)
    exit(0)
elif "-h" in args or "--help" in args:
    print("Print out the passed arguments, 1 on each line")
    exit(0)

#print args
for a in args:
    print(a)
