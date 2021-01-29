import os, sys

if len(sys.argv)<2:
    print("Please prove the path to a file containing a number sequence")

fp = sys.argv[1]

with open(fp,"r") as f:
    words = f.read().split()
    
for word in words:
    if not word.isdigit():
        continue
    bin_string = "{:08b}".format(int(word))
    #print binary string with 1->'#' 0->' '
    print(bin_string.replace('1','#').replace('0',' '))
