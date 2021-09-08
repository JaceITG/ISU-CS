#!/usr/bin/env python3

import sys

def gcd(a,b):
    if b==0:
        print("Error: b cannot be zero")
    r=a%b
    if r==0:
        return b
    a=b
    b=r
    return gcd(a,b)

if __name__ == "__main__":
    args = sys.argv
    if len(args)<3 or not args[1].isdigit() or not args[2].isdigit():
        print("Usage: gcd.py a b")
        sys.exit(0)
    a=int(args[1])
    b=int(args[2])
    print(f"GCD of {a} and {b} = {gcd(a,b)}")
