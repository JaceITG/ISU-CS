from parsegraph import graph #graph parsing script from Isaiah Bartlett

#Detect the existence of a directed cycle in passed digraph D (file)
def directed_cycle(D, start=None):
    adj, first, searchType = graph(D)
    
    #if none passed, take first vertex from parser
    if not start:
        start = int(first)
    
    #create a stack
    stk = [start]
    explored = [False for point in adj] #pad out explored list with zeros

    while len(stk) > 0:
        u = stk.pop()
        #print(f"popping {u}")

        if explored[u] and u == start:
            print(f"Directed cycle found")
            return
        elif not explored[u]:
            explored[u] = True
            #for every edge in u's adjacency
            for i in range(len(adj[u])):
                if adj[u][i]==1:
                    stk.append(i)
    
    print("No cycle found through vertex " + str(start))
    return

if __name__ == "__main__":
    directed_cycle('inputdir.txt', 4)
