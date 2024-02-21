count=int(input())
result=[]
for _ in range(count):
    n,m= map(int, input().split())
    graph=[]
    data=list(map(int, input().split()))
    index=0
    for _ in range(n):
        graph.append(data[index:index+m])
        index+=m
    for j in range(1,m):
        for i in range(n):
            temp_list=[]
            for k in range(i-1,i+2):
                if k>=0 and k<n:
                    temp_list.append(graph[k][j-1])
            graph[i][j]=graph[i][j]+max(temp_list)
    result.append(max(x[m-1] for x in graph))
for i in range(len(result)):
    print(result[i])