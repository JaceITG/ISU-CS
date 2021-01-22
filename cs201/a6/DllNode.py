#!/usr/bin/env python3

class Node:

    def __init__(self,val):
        self.value = val
        self.prev = None
        self.next = None

if __name__ == "__main__":


    a = Node("a")
    b = Node("b")
    c = Node("c")

    a.next = b
    b.prev = a
    b.next = c
    c.prev = b

    print("==== Forward ====")
    printing = a
    while printing:
        print(printing.value)
        printing = printing.next

    print("==== Backward ====")
    printing = c
    while printing:
        print(printing.value)
        printing = printing.prev
