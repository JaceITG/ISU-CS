#!/usr/bin/env python3

import math
import sys

class Node:
    def __init__(self, value):
        # should have 3 attributes:
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.length = 0


    def __len__(self):
        return self.length


    def get_node(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range.")

        i = 0
        visit_queue = [self.root]
        current_node = visit_queue.pop(0)

        while i < index:
            if current_node.left:
                visit_queue.append(current_node.left)
            if current_node.right:
                visit_queue.append(current_node.right)
            current_node = visit_queue.pop(0)
            i+= 1

        return current_node


    def get_value(self, index):
        return self.get_node(index).value


    def insert(self, value):
        new_node = Node(value)

        if len(self) == 0:
            #New Root
            self.root = new_node
            self.length += 1
            return

        i = 0
        queue = [self.root]
        current_node = queue.pop(0)
        #Loop through tree looking for first node without child
        while i < len(self):
            if current_node.left:
                queue.append(current_node.left)
            else:
                current_node.left = new_node
                self.length += 1
                return
            if current_node.right:
                queue.append(current_node.right)
            else:
                current_node.right = new_node
                self.length += 1
                return

            current_node = queue.pop(0)
            i += 1
        return

    def remove(self):
        if len(self) == 0:
            raise IndexError("Cannot remove from empty tree")

        index_last = len(self)-1
        index_parent = (index_last-1)//2
        #If the parent index calculation has no remainder, is left child
        is_left_child = (index_last-1)%2 != 1

        if is_left_child:
            self.get_node(index_parent).left = None
        else:
            self.get_node(index_parent).right = None
        self.length -= 1

    def breadth_first_traversal(self):
        traversal = []
        if len(self) == 0:
            return traversal

        for i in range(len(self)):
            traversal.append(self.get_value(i))
        return traversal


    def _dft_visit(current_node, traversal, order_type):
        #Preorder append
        if order_type == "preorder":
            traversal.append(current_node.value)

        if current_node.left:
            #Visit left
            Tree._dft_visit(current_node.left,traversal,order_type)

        #Inorder append
        if order_type == "inorder":
            traversal.append(current_node.value)

        if current_node.right:
            #Visit right
            Tree._dft_visit(current_node.right,traversal,order_type)

        #Postorder append
        if order_type == "postorder":
            traversal.append(current_node.value)


    def depth_first_preorder_traversal(self):
        traversal = []
        Tree._dft_visit(self.root,traversal,"preorder")
        return traversal


    def depth_first_inorder_traversal(self):
        traversal = []
        Tree._dft_visit(self.root,traversal,"inorder")
        return traversal


    def depth_first_postorder_traversal(self):
        traversal = []
        Tree._dft_visit(self.root,traversal,"postorder")
        return traversal


    def breadth_first_search_node(self, search_value):
        i = 0
        visit_queue = [self.root]
        current_node = visit_queue.pop(0)

        while i < len(self):
            if current_node.left:
                visit_queue.append(current_node.left)
            if current_node.right:
                visit_queue.append(current_node.right)
            current_node = visit_queue.pop(0)
            if current_node.value == search_value:
                return current_node
            i+= 1

        return None


    def _dfs_visit(current_node, search_value):
        if current_node.value == search_value:
            return current_node

        if current_node.left:
            #Visit left
            found = Tree._dfs_visit(current_node.left,search_value)
            if found:
                return found

        if current_node.right:
            #Visit right
            found = Tree._dfs_visit(current_node.right,search_value)
            if found:
                return found

        return None


    def depth_first_search_node(self, search_value):
        return Tree._dfs_visit(self.root, search_value)


    def _tree_print_recursion(self, level=0, index=0, width=80):
        num_on_level = 2**level
        term_i = 0
        for i in range(num_on_level):
            val = self.get_value(index)
            pos = (i+1) * (width / (num_on_level + 1))
            glyph = "("+str(val)+")"
            multiplier = math.floor(pos - term_i - len(glyph)/2)
            term_i += multiplier + len(glyph)
            padding = " " * multiplier
            print(padding + glyph, end="")
            index += 1
            if index >= len(self):
                break
        print()
        print("-"*width)
        if index <  len(self):
            self._tree_print_recursion(level+1, index, width)


    def tree_print(self, width=80):
        print("="*width)
        self._tree_print_recursion(0, 0, width)


if __name__ == "__main__":

    t = Tree()

    if "value" not in dir(Node("test")):
        print("Complete the Node class to continue testing.")
        sys.exit(0)

    # Remove or comment out the manual tree construction once you have completed Tree.insert()
    # t.root = Node("a")
    # t.length+= 1
    # t.root.left = Node("b")
    # t.length+= 1
    # t.root.right = Node("c")
    # t.length+= 1
    # t.root.left.left = Node("d")
    # t.length+= 1
    # t.root.left.right = Node("e")
    # t.length+= 1
    # t.root.right.left = Node("f")
    # t.length+= 1
    # t.root.right.right = Node("g")
    # t.length+= 1

    # Uncomment once you have completed Tree.insert() to automatically construct the tree with insert()
    ascii_a_ordinal = 97
    number_nodes = 15
    for i in range(ascii_a_ordinal, ascii_a_ordinal + number_nodes):
        t.insert(chr(i))

    t.tree_print()

    print("Breadth First Traversal:")
    print(t.breadth_first_traversal())
    print("Depth First Preorder Traversal:")
    print(t.depth_first_preorder_traversal())
    print("Depth First Inorder Traversal:")
    print(t.depth_first_inorder_traversal())
    print("Depth First Postorder Traversal:")
    print(t.depth_first_postorder_traversal())
    print()

    print('Breadth First Search for "f":')
    n = t.breadth_first_search_node("f")
    if n != None:
        print(n.value, "Found!")
    else:
        print("Not found.")

    print('Depth First Search for "g":')
    n = t.depth_first_search_node("g")
    if n != None:
        print(n.value, "Found!")
    else:
        print("Not found.")

    t.remove()
    t.remove()
    t.remove()
    t.tree_print()
