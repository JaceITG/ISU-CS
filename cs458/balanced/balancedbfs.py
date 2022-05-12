from parsegraph import graph #graph parsing script from Isaiah Bartlett

def is_balanced(G, start=None):
    adj, first, searchType = graph(G)

    #if none passed, take first vertex from parser
    if not start:
        start = int(first)
    
    #create a queue
    qu = [start]
    level = [None for point in adj] #pad out level list with zeros
    level[start] = 0 #start vertex at level zero

    while len(qu) > 0:
        u = qu.pop(0)
        #print(f"popping {u}")

        #look at all arcs of u
        for i in range(len(adj[u])):
            
            if adj[u][i]==1:
                #arc ui exists

                if level[i] and level[i] != (level[u]+1):
                    #if u has arc to vertex i that exists on a nonsuccessive level
                    return False
                
                #iniitialize i with level one greater than u
                level[i] = level[u]+1
                qu.append(i)
    return True


if __name__ == "__main__":
    print("Balanced" if is_balanced('inputbal.txt') else "Not Balanced")
    print("Balanced" if is_balanced('inputnotbal.txt') else "Not Balanced")
