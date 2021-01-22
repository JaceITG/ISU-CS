#!/usr/bin/env python3

import sys

args = sys.argv[1:]

unsorted_numbers = []
if len(args):
    for arg in args:
        x = float(arg)
        unsorted_numbers.append(x)
else:
    s = input("Enter a number (blank to quit): ")
    while len(s) > 0:
        x = float(s)
        unsorted_numbers.append(x)
        s = input("Enter a number (blank to quit): ")

# FINISH THIS - function to move an element at the index1 location of the list to the index2 location, and then also the element from index2 location to the index1 location.
def swap(li, index1, index2):
    li[index1],li[index2] = li[index2],li[index1]

# MODIFY THIS
def my_sort(unsorted):
    # For each sorting algorithm, modify this function to sort your numbers
    work = 0
    sorted = list(unsorted)

    for i in range(1,len(sorted)):
        value = sorted[i]
        currIndex = i

        #while preceding value is less than current val, move preceding
        #value up one index
        while currIndex > 0 and sorted[currIndex-1] > value:
            sorted[currIndex] = sorted[currIndex-1]
            currIndex -= 1
            work += 1
        #insert the value at the correct current index
        sorted[currIndex] = value

    return sorted, work


if __name__ == "__main__":
    print(f'Running "{__file__}..."')
    sorted_numbers, work = my_sort(unsorted_numbers)
    python_sorted = list(unsorted_numbers)
    python_sorted.sort()
    print("Unsorted:")
    print("   ", unsorted_numbers)
    print("Sorted:")
    print("   ", sorted_numbers)
    print("Python Sorted:")
    print("   ", python_sorted)
    if sorted_numbers == python_sorted:
        print("Sort SUCCEEDED!")
    else:
        print("Sort FAILED!")
    print(f"The list of length {len(unsorted_numbers)} required {work} units of work to sort.")

    # MODIFY THIS - time complexity of the algorithm based on the lecture material. https://www.bigocheatsheet.com/
    timeComplexity = "n**2" # Example time complexity

    print(f"The time complexity of this sort is Big-O({timeComplexity})")
