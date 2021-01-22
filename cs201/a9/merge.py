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

# helper function to merge two sorted arrays
def merge(a,b):
    sorted = []

    #Append beginnings of both arrays to sorted array
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            sorted.append(b.pop(0))
        else:
            sorted.append(a.pop(0))

    #sort leftover values
    while len(a) > 0:
        sorted.append(a.pop(0))

    while len(b) > 0:
        sorted.append(b.pop(0))

    return sorted


# MODIFY THIS
def my_sort(unsorted, work):
    # For each sorting algorithm, modify this function to sort your numbers
    sorted = list(unsorted)
    length = len(sorted)

    #Base case
    if length == 1:
        return sorted, work

    left = list(sorted[:length//2])
    right = list(sorted[length//2:])

    #Sort each side
    left, work = my_sort(left, work)
    work += 1
    right, work = my_sort(right, work)
    work += 1

    return merge(left,right), work


if __name__ == "__main__":
    print(f'Running "{__file__}..."')
    sorted_numbers, work = my_sort(unsorted_numbers, 0)
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
    timeComplexity = "n * log(n)" # Example time complexity

    print(f"The time complexity of this sort is Big-O({timeComplexity})")
