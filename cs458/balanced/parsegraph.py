import sys
import random
def graph(file):
    try:
        f = open(file) # open formatted input file with data
    except FileNotFoundError:
        if file == '': # if you purposefully didn't put a file, use the default graph
            print('No file specified, using default graph\n')
            z = 0
            t1 = [
            [z, 1, 1, z, 1, z, z],
            [z, z, 1, 1, z, 1, z],
            [z, z, z, z, z, 1, 1],
            [1, z, z, z, 1, z, z],
            [1, z, z, z, z, z, 1],
            [z, z, z, z, 1, z, 1],
            [z, z, z, z, z, z, z]
            ]
            adj = t1 # easy to debug having different tables with vars
            print(f"default graph:")
            print('-' * 30)
            for x in range(len(adj)):
                print(f"point {x}: {adj[x]}") # print the graph row by row
            print('-' * 30)
            searchType = input("Would you like to use [bfs] or [dfs]: ")
            return adj, random.randint(0, len(adj) - 1), searchType
        else:
            sys.exit(f'File "{file}" not found.')
    n = f.readline().split() # number of points at head of the file space-seperated by the starting point 0-indexed, and the search type.
    if len(n) != 3:
        sys.exit("Incorrect file syntax")
    start = n[1]
    searchType = n[2]
    n = int(n[0])
    adj = [[0 for x in range(n)] for y in range(n)] # make an empty matrix of size n
    line = f.readline().split() # read and seperate the data
    while line:
        if len(line) != 2: # verify the data
            sys.exit("Incorrect file syntax")
        v = int(line[0])   #            ]
        out = int(line[1]) # write data |
        adj[v][out] = 1    #            ]
        line = f.readline().split()
    f.close()
    print(f'Graph from input file "{file}" 0-indexed:')
    print('-' * 30)
    for x in range(n):
        print(f"point {x}: {adj[x]}")
    print('-' * 30)
    return adj, start, searchType