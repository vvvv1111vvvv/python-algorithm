from collections import deque
import sys
def bfs(x,k, graph, visited):
    q=deque([[x,0]])
    visited[x]=True
    result=[]
    while q:
        now=q.popleft()
        if now[1]==k:
            result.append(now[0])
            continue
        for i in graph[now[0]]:
            if visited[i]==False:
                q.append([i,now[1]+1])
                visited[i]=True
    return result
n,m,k,x=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for _ in range(m):
    a,b=map(int, sys.stdin.readline().split())
    graph[a].append(b)
cities=bfs(x,k,graph,visited)
if len(cities)==0:
    print(-1)
else:
    for city in sorted(cities):
        print(city)
