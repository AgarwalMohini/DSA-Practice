from typing import List
from collections import deque

def bfsTraversal(n: int, adj: List[List[int]]) -> List[int]:
    # write your code here
    bfs=[]
    q=deque()
    vis=[False] * n
    q.append(0)
    vis[0]=True
    while q:
        node=q.popleft()
        bfs.append(node)

        for it in adj[node]:
            if not vis[it]:
                vis[it]=True
                q.append(it)
    return bfs
    pass