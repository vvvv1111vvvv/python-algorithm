from collections import deque
def bfs(s,x,y,graph,n,k, virous,visited):
    count=0
    q=deque()
    nq=deque()
    for i in range(1,len(virous)):
        if len(virous[i])!=0:
            for j in virous[i]:
                q.append([i, j])
                visited[j[0]][j[1]]=True
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    while count<s:
        while q:
            now=q.popleft()
            for i in range(4):
                nx=now[1][0]+dx[i]
                ny=now[1][1]+dy[i]
                if nx<1 or ny<1 or nx>n or ny>n:
                    continue
                if visited[nx][ny]==True:
                   continue
                graph[nx][ny]=now[0]
                visited[nx][ny]=True
                nq.append([now[0],[nx,ny]])
        if len(nq)!=0:
            q=deque()
            for i in nq:
                q.append(i)
            nq=deque()
        count+=1
    return graph[x][y]
n,k = map(int, input().split())
graph=[[0]*(n+1)]
visited=[[False]*(n+1) for _ in range(n+1)]
virous=[[] for _ in range(k+1)]
for i in range(1,n+1):
    graph.append([0]+list(map(int, input().split())))
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]!=0:
            virous[graph[i][j]].append([i,j])    
s,x,y= map(int, input().split())
print(bfs(s,x,y,graph,n,k, virous,visited))
