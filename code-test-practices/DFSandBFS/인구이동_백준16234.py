from collections import deque
def distribute():
    dist_count=0
    for i in range(len(union_group)):
        total_union_pop=0
        for x,y in union_group[i]:
            total_union_pop+=pop[x][y]
        divided_pop=int(total_union_pop/len(union_group[i]))
        for x,y in union_group[i]:
            if pop[x][y]==divided_pop:
                continue
            pop[x][y]=divided_pop
            dist_count+=1
    if dist_count==0:
        return False
    else: 
        return True
def bfs():
    visited=[[False]*(n) for _ in range(n)]
    union_group=[]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q=deque()
                q.append([i,j])
                temp_u=[[i,j]]
                visited[i][j]=True
                dx=[-1,0,1,0]
                dy=[0,-1,0,1]
                while q:
                    x,y=q.pop()
                    for k in range(4):
                        nx=x+dx[k]
                        ny=y+dy[k]
                        if nx<0 or ny<0 or nx>=n or ny>=n:
                            continue
                        if visited[nx][ny]:
                            continue
                        if abs(pop[x][y]-pop[nx][ny])>=l and abs(pop[x][y]-pop[nx][ny])<=r:
                            q.append([nx,ny])
                            temp_u.append([nx,ny])
                            visited[nx][ny]=True
                if len(temp_u)>1:
                    union_group.append(temp_u)
    return union_group

n,l,r=map(int, input().split())
pop=[]
for i in range(n):
    pop.append(list(map(int, input().split())))
count=0
while True:
    union_group=bfs()
    if len(union_group)==0:
        break
    if not distribute():
        break
    count+=1
print(count)
          
      