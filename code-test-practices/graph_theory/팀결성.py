n,m=map(int, input().split())
result=[]
parent=[0]*(n+1)
def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a,b):
    a= find_parent(parent, a)
    b=find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
for i in range(1,n+1):
    parent[i]=i
for _ in range(m):
    x, a, b= map(int, input().split())
    if x==0:
        union_parent(parent, a,b)
    if x==1:
        if find_parent(parent,a)== find_parent(parent,b):
            result.append("YES")
        else:
            result.append("NO")
for i in result:
    print(i, end='\n')