####################################################################
###
### Author: Jose Moran 
### Email : jmoran071996@gmail.com
### Github: jose0796
### Description: Graphs Algorithms implementations
###
####################################################################


def bfs(g,s):
    level = {s:0}
    parent = {s:None}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in g[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next 
        i+=1

    return parent

def path(p,s):
    pp = []
    print(p[s])
    while p[s] != None:
        pp.append(s)
        s = p[s]
        
    return pp



