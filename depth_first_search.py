# Depth First Search example program
import sys

def adjacent_points(G, point):
    (V, E) = G
    neighbors = set()
    for e in E:
        if point in e :
            if e[0] == point :
                neighbors.add(e[-1])
            else:
                neighbors.add(e[0])
    return neighbors

def DFSearch(G, start_point):
    (V, E) = G
    if not start_point in V :
        print('Error: the starting point '+str(start_point)+' is not in G.')
        return ()
    E_T = set()
    sta = [start_point]
    d = dict() # 0 <= d[point] < |V| ... visited
    for l in V:
        d[l] = len(V) # more than maximum distance
    d[start_point] = 0
    # print(d, que)
    while len(sta) != 0 :
        v = sta[-1]
        for w in adjacent_points(G, v):
            if d[w] == len(V):
                print( (v, w) )
                d[w] = d[v] + 1
                sta.append(w)
                E_T.add( (v,w) )
                break
        else:
            sta.pop()
        print(sta)
    return (V, E_T)

V = eval(sys.argv[1])
E = eval(sys.argv[2])
if len(sys.argv) > 3 :
    start_point = eval(sys.argv[3])
else:
    start_point = sorted(list(V))[0]
G = (V, E)

print('G='+str(G), 'start = ' + str(start_point))

print(DFSearch(G, start_point))

#
#"{1, 2, 3, 4, 5, 6, 7}"
#"{(1,2), (2,3), (3,4), (3,6), (1, 4), (2, 5), (5,6), (1,5), (4,7)}"
#
