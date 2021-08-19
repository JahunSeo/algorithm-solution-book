def BFS(s, Adj):
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]  # level == i-1
    while frontier:
    	next = []   # level == i
        for u in frontier:
            for v in Adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1