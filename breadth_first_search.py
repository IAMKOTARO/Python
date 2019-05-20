# Breadth First Search example program
import sys
from pickle import FALSE
def adjacent_points(G, point):
    (V, E) = G
    neighbors = set()
    for e in E:
        if point in e :
            if e[0] == point :
                neighbors.add(e[-1]) # the other (2nd) end point
            else:
                neighbors.add(e[0])  # the 1st end point
    return neighbors

def BFSearch(G, start, show = False):
    (V, E) = G
    if not start in V :
        print('Error: the starting point '+str(start)+' is not in G.')
        return ()
    E_T = set()
    que = [start]  # the initial front line
    d = dict() # 0 <= d[point] < |V| ... visited
    for l in V:
        d[l] = len(V) # U = the empty set
    d[start] = 0
    # print(d, que)
    while len(que) != 0 :
        v = que.pop(0)
        for w in adjacent_points(G, v) :
            # print( (v, w) )
            if d[w] != len(V) : # iv w is in U
                continue
            d[w] = d[v] + 1  # add w to U
            que.append(w)
            E_T.add( (v,w) )
        if show: print(que) # show the current front line 
    return (V, E_T)

V = eval(sys.argv[1])
E = eval(sys.argv[2])
if len(sys.argv) > 3 :
    start_point = eval(sys.argv[3])
else:
    start_point = sorted(list(V))[0]
G = (V, E)

print('G='+str(G), 'start = ' + str(start_point))

print('Spanning Tree =', BFSearch(G, start_point))
