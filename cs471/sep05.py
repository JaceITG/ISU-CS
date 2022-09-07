import sys

EMPTY = -1

def main():

    maxblock = int(sys.argv[1])
    minblock = int(sys.argv[2])

    #initialize tree
    buddytree = [
        {'pid': EMPTY, 'address': 0, 'size': maxblock, 'left': None, 'right': None}
    ]

    print_tree(buddytree)

    while True:
        #get input for memory transaction
        req = input()
        args = req.split(' ')

        if args[0] == 'A':
            #allocate
            pid = int(args[1])
            size = int(args[2])

            buddytree = allocate(buddytree, pid, size, minblock)

            print_tree(buddytree)


        elif args[0] == 'D':
            #free mem
            pid = int(args[1])
            index=-1
            #find index of process in tree
            for ind, item in enumerate(buddytree):
                if item['pid'] == pid:
                    index = ind
                    break
            
            buddytree[index]['pid'] = EMPTY
            buddytree = merge(buddytree,index)

            print_tree(buddytree)

#Branch an empty slot into two slots of half the size
def split(tree, index):

    before = tree[:index]
    after = tree[index+1:]

    old_size = tree[index]['size']
    old_add = tree[index]['address']
    new_slots = [
        {'pid': EMPTY, 'address': old_add, 'size': old_size//2},
        {'pid': EMPTY, 'address': old_add+(old_size//2), 'size': old_size//2}
    ]

    newtree = before + new_slots + after
    return newtree

def merge(tree, index):
    size = tree[index]['size']
    buddy = tree[index]['address'] ^ size

    #get index of same-sized buddy in list
    buddy_index = -1
    for ind, item in enumerate(tree):
        if item['address'] == buddy and item['pid'] == EMPTY and item['size'] == size:
            buddy_index = ind
            break
    
    #if buddy found
    if buddy_index>=0:
        #make a new tree combining the buddies
        start_ind = min(index, buddy_index)
        newtree = tree[:start_ind]

        newtree += [{'pid': EMPTY, 'address': tree[start_ind]['address'], 'size': size*2}]   #block combining two buddies

        newtree += tree[max(index,buddy_index)+1:]
        
        #recursively check if merged block can be merged again
        newtree = merge(newtree, start_ind)
        return newtree
    else:
        #no buddy to be merged, return tree
        return tree


def allocate(tree, pid, size, minblock):
    
    #Find the first smallest available block in the tree for new segment
    block = None
    smallest = 0xfffffff
    for ind, item in enumerate(tree):
        if item['pid'] == EMPTY:
            if item['size'] < smallest and item['size'] >= size:
                smallest = item['size']
                block = ind

    if block is None:
        print(f"Not enough memory to allocate process {pid} with size {size}")
        return
    
    #while the selected block can be split in half
    while tree[block]['size'] >= size*2 and tree[block]['size']//2 >= minblock:
        tree = split(tree, block)
        #new index is one greater after splitting
        block += 1
    
    #allocate block in tree as pid
    tree[block]['pid'] = pid
    return tree

def print_tree(tree):
    
    for ind, item in enumerate(tree):
        #print pid
        pid = item['pid']
        print(f"{pid}" if pid>EMPTY else " ", end=' | ')

        #print address
        print(f"{item['address']:06b} {item['address']:>3}", end=" | ")

        #print size
        print(f"{item['size']:06b} {item['size']:>3}")

    
    

if __name__ == "__main__":
    main()