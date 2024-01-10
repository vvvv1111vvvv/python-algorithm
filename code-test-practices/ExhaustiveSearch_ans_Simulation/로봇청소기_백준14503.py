def cleaning(data,first_r,first_c,first_d):
    stack=[[first_r,first_c]]
    direction=first_d
    count=0
    while stack:
        val=stack.pop()
        if data[val[0]][val[1]]==0:
            data[val[0]][val[1]]=2
            count+=1
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        flag=False
        for i in range(direction-1,direction-5,-1):
            nx=val[0]+dx[i%4]
            ny=val[1]+dy[i%4]
            if data[nx][ny]==0:
                stack.append([nx,ny])
                flag=True
                direction=i%4 
                break
        if flag==False:
            nx=val[0]-dx[direction]
            ny=val[1]-dy[direction] 
            if data[nx][ny]==2:
                stack.append([nx,ny])
            else:
                return count
             
                
            
        
    
n,m=map(int, input().split())
first_r,first_c,first_d=map(int, input().split())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))
print(cleaning(data,first_r,first_c,first_d))
