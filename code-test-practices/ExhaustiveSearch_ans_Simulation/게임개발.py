n,m=map(int, input().split(" "))
visit=[[0]*m for _ in range(n)]
a,b,d=map(int, input().split(" "))

visit[a][b]=1
count=1
gmap=[]

#visit=[[0 for column in range(m)] for row in range(n)]
for i in range(n):
    temp=list(map(int, input().split()))
    gmap.append(temp)

na=0
nb=0
while True:
    current=(a,b,d)
    #갈 곳을 정하는 부분
    for j in range(4):
        d-=1
        if(d<0):
            d=3-d
        if(d==0):
            na,nb=a-1, b            
        elif(d==1):
            na,nb=a,b+1
        elif(d==2):
            na,nb=a+1,b
        elif(d==3):
            na,nb=a,b-1
        if(visit[na][nb]==0 and gmap[na][nb]==0):
            a,b=na,nb
            visit[na][nb]=1
            count+=1
            break
    #후진하는 부분
    if current[0]==a and current[1]==b:
        if(d==0):
            na,nb=a+1,b
        elif(d==1):
            na,nb=a,b-1
        elif(d==2):
            na,nb=a-1,b
        elif(d==3):
            na,nb=a,b+1
        if(gmap[na][nb]==1):
            break
print(count)

