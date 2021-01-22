#!/usr/bin/env python3

import sys,DoublyLinkedList

class Queue(DoublyLinkedList.DoublyLinkedList):
    def __init__(self,list=None):
        super().__init__(list)

    def add(self, value):
        self.append(value)

    def remove(self):
        return self.pop(0)

if __name__ == "__main__":
    queue = Queue()
    queue.add("a")
    queue.add("b")
    queue.add("c")
    print(queue.remove())
    print(queue.remove())
    print(queue.remove())
