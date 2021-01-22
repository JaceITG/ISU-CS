#!/usr/bin/env python3

import sys,DoublyLinkedList

class Stack(DoublyLinkedList.DoublyLinkedList):
    def __init__(self,list=None):
        super().__init__(list)

    def add(self, value):
        self.insert(0,value)

    def remove(self):
        return self.pop(0)

if __name__ == "__main__":
    stk = Stack()
    stk.add("a")
    stk.add("b")
    stk.add("c")
    print(stk.remove())
    print(stk.remove())
    print(stk.remove())
