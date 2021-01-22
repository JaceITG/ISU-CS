#!/usr/bin/env python3

import sys
args = sys.argv[1:]

#Check for args passed
if len(args):
    #Use arguments as list to sort
    str_list = args
    nums_list = []
    for i in str_list:
        nums_list.append(float(i))

else:
    #Get arguments from stdin
    nums_list = []

    while True:
        num = input("Enter a number (leave blank to quit): ")

        if num:
            try:
                nums_list.append(float(num))
            except:
                raise Exception("Input must be an integer or float value")
                sys.exit()
        else:
            break



#Remove and return the lowest number in the list
def getLowest(nums_list, work):
    lowest = None
    for i in nums_list:
        work+=1
        if lowest == None or i < lowest:
            lowest = i
    nums_list.remove(lowest)
    return lowest,work

print(nums_list)
sorted = []
#While there are nums in the list
work = 0
while len(nums_list):
    #Add the lower number in list to sorted list
    lowest,work = getLowest(nums_list,work)
    sorted.append(lowest)

print(sorted)
print("Complexity: O(n^2)")
print(f"Work: {work}")
