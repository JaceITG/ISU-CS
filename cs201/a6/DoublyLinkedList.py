#!/usr/bin/env python3

import sys
from DllNode import Node

class DoublyLinkedList:
    def __init__(self,list=None):
        self._length = 0
        self.start = None
        self.end = None

        if type(list)==type(self):
            #Duplicate passed DLL and add at beginning
            self.addDll(0,list)
        elif type(list)==type([]):
            #Add values from a list
            for item in list:
                self.append(item)



    def __len__(self):
        return self._length

    def get_node(self, index):
        if index >= self._length or index < 0:
            return None

        if index < (self._length / 2):
            #Loop forwards
            current_node = self.start
            for i in range(index):
                #If current node is None, break to avoid calling
                #None.next
                if not current_node:
                    break
                current_node = current_node.next
            return current_node
        else:
            #Loop backwards
            current_node = self.end
            for i in range(self._length-index-1):
                #If current node is None, break to avoid calling
                #None.prev
                if not current_node:
                    break
                current_node = current_node.prev
            return current_node

    def get_value(self, index):
        return self.get_node(index).value

    def append(self, val):
        node = Node(val)
        if not self.start:
            #If list is empty (has no start), make start this node
            self.start = node
        else:
            #If one or more nodes in list, link them
            self.end.next = node
            node.prev = self.end
        self.end = node
        self._length += 1

    def insert(self, index, val):
        if index > self._length:
            raise Exception(f"Index {index} out of bounds")

        node = Node(val)
        #Check for a previous and next node
        next = self.get_node(index)
        prev = self.get_node(index-1)

        #The next will be the one currently at index
        if prev:
            prev.next = node
            node.prev = prev
        else:
            #Node will be at start
            self.start = node

        if next:
            next.prev = node
            node.next = next
        else:
            #Node is at end
            self.end = node
        self._length += 1

    def pop(self, index):
        node = self.get_node(index)
        if not node:
            print(f"Error: node at index {index} does not exist",file=sys.stderr)
        else:
            value = node.value

            if self._length == 1:
                #Only node in list, unlink all
                self.start = None
                self.end = None
            else:
                node_next = node.next
                node_prev = node.prev

                #Link nodes on either side
                if node_prev:   #If it has a previous
                    node_prev.next = node_next
                else:
                    #Change start node
                    self.start = node_next

                if node_next:   #If it has a next
                    node_next.prev = node_prev
                else:
                    #Change end node
                    self.end = node_prev
            self._length -= 1
            return value

    def remove(self,value):
        #Find node with given val
        current_node = self.start
        node = None
        while current_node:
            if current_node.value == value:
                node = current_node
                break
            else:
                current_node = current_node.next

        if not node:
            print(f"Error: node with value {value} not found",file=sys.stderr)
        elif self._length == 1:
            #Only node in list, unlink all
            self.start = None
            self.end = None
        else:
            node_next = node.next
            node_prev = node.prev

            #Link nodes on either side
            if node_prev:   #If it has a previous
                node_prev.next = node_next
            else:
                #Change start node
                self.start = node_next

            if node_next:   #If it has a next
                node_next.prev = node_prev
            else:
                #Change end node
                self.end = node_prev
        self._length -= 1

    def print_forward(self):
        current_node = self.start
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def print_backward(self):
        current_node = self.end
        while current_node:
            print(current_node.value)
            current_node = current_node.prev

    def addDll(self, position, dll):
        for i in range(len(dll)):
            current_value = dll.get_value(i)
            self.insert(position+i,current_value)


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append("b")
    dll.insert(1, "c")
    dll.insert(0, "a")
    dll.append("d")
    dll.remove("d")

    print("==== Forward ====")
    dll.print_forward()
    print("==== Backward ====")
    print(dll.pop(len(dll)-1))
    print(dll.pop(len(dll)-1))
    print(dll.pop(len(dll)-1))
