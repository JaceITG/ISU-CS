import random
RADIUS = 2      #radius of tower coverage

#added value of new buildings covered by a tower placed at x
def value_added(y, previous):
    global b,v

    #whether building bu is in range of tower at p
    in_range = lambda bu,p: (bu<p and bu+RADIUS>=p) or (bu>p and bu-RADIUS<=p)

    total = 0
    for i in range(len(b)):
        if in_range(b[i],y) and (not previous or not in_range(b[i], previous)):
            #cover building at index i
            total += v[i]

    return total



#Maximum coverage amount up to last point x with t towers
def cover(x, t, d):
    #base case: if no towers, no coverage possible
    if t == 0 or x <= 0:
        return 0
    
    #check all placements for y <= x
    max_cover = (-1, -1)
    for y in range(x):
        #don't allow tower placement on building positions
        if y in b:
            continue

        #add the optimal coverage up to next endpoint, to the value of a tower at this point
        coverage = cover(y, t-1, d+1) + value_added(y, x if d>0 else None)  #if towers have already been placed, use endpoint as a previous tower to satisfy buildings

        #update if coverage is greater
        if coverage>max_cover[1]:
            max_cover = (y, coverage)
    
    print(f"Best placement ({x}, {t}) for recr depth {d}: point {max_cover[0]} worth {max_cover[1]}")
    return max_cover[1]

if __name__ == "__main__":
    global b,v

    b1 = []
    v1 = []
    while len(b1) < 6:
        pos = random.randint(0,15)
        val = random.randint(1, 41)
        if pos not in b1 and val not in v1:
            b1.append(pos)
            v1.append(val)
    b2 = [3,5,6,8,12,14]
    v2 = [5,9,1,13,2,40]

    b3 = [4,8,12,13,16,20,25,29]
    v3 = [15,8,12,1,22,4,5,41]
    print(f"{sorted(b1)} # building placements\n{v1} # values")
    b = sorted(b1)
    v = v1

    #Maximum coverage up to the last building in b with 4 towers
    print(f"Best coverage: {cover(17, 3, 0)}")
    