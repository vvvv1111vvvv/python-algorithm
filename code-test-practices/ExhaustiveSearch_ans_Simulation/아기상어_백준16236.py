from collections import deque
def find_dist(n,shark_size_loc,fish_size_loc,possible_fish):
    t_dist=[]
    for p_fish in possible_fish:
        dq=deque([shark_size_loc[1]])
        t_count=[[0]*n for _ in range(n)]
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        
        while dq:
            nw_loc=dq.popleft()
            if (nw_loc[0], nw_loc[1]) == (p_fish[1][0],p_fish[1][1]):
                t_dist.append([p_fish,t_count[nw_loc[0]][nw_loc[1]]])
                break
            for i in range(4):
                nx=nw_loc[0]+dx[i]
                ny=nw_loc[1]+dy[i]
                if nx<0 or ny<0 or nx>=n or ny>=n or d[nx][ny]>shark_size_loc[0]:
                    continue
                if t_count[nx][ny]==0:
                    t_count[nx][ny]=t_count[nw_loc[0]][nw_loc[1]]+1
                    dq.append([nx,ny])
    if len(t_dist)==0:
        return None
    t_dist.sort(key= lambda x: (x[1],x[0][1][0],x[0][1][1]))
    return t_dist[0]
            
n=int(input())
d=[]
fish_size_loc=[]
possible_fish=[]
count=0
for i in range(n):
    d.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if d[i][j]==9:
            shark_size_loc=[2, [i,j],0]
        elif d[i][j]!=0:
            fish_size_loc.append([d[i][j],[i,j]])
d[shark_size_loc[1][0]][shark_size_loc[1][1]]=0
for i in range(len(fish_size_loc)):
    possible_fish=[]
    for j in range(len(fish_size_loc)):
        if fish_size_loc[j][0]<shark_size_loc[0]:
            possible_fish.append(fish_size_loc[j])
    if len(possible_fish)==0:
        break
    val=find_dist(n,shark_size_loc,fish_size_loc,possible_fish)
    if val is None:
        break
    count+=val[1]
    shark_size_loc=[shark_size_loc[0],[val[0][1][0],val[0][1][1]],shark_size_loc[2]+1]
    if shark_size_loc[0]==shark_size_loc[2]:
        shark_size_loc[2]=0
        shark_size_loc[0]+=1     
    fish_size_loc.remove([d[val[0][1][0]][val[0][1][1]],[val[0][1][0],val[0][1][1]]])
    d[shark_size_loc[1][0]][shark_size_loc[1][1]]=0
print(count)

