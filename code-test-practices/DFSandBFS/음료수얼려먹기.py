n,m=map(int, input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(v,w):
    if v<0 or v>=n or w<0 or w>=m:
        return
    
    if graph[v][w]==0 and visited[v][w]==False:
        visited[v][w]=True
        dfs(v+1,w)
        dfs(v-1,w)
        dfs(v,w+1)
        dfs(v,w-1)
    
count=0

visited=[[False]*m for _ in range(n)]
for i in range (n):
    for j in range(m):
        if graph[i][j]==0 and visited[i][j]==False:
            count+=1
            dfs(i,j)
print(count)