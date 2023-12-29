n,m= map(int, input().split())
INF= int(1e9)
edges=[]
result=0
last=0
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i
for _ in range(m):
    a,b,c= map(int, input().split())
    edges.append((c,a,b))
edges.sort()
def find_parent(parent,a):
    if parent[a]!=a:
        parent[a]=find_parent(parent, parent[a])
    return parent[a]
def union_parent(parent, a, b):
    a=find_parent(parent, a)
    b=find_parent(parent, b)   
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
for edge in edges:
    cost,a,b=edge
    if find_parent(parent, a)==find_parent(parent,b):
        continue
    union_parent(parent, a,b)
    result+=cost
    last=cost
print(result-last)