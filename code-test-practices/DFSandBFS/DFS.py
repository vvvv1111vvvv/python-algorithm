def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if visited[i]==False:
            dfs(graph, i, visited)
graph=[
    [],
    [2, 3, 8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9
dfs(graph, 1, visited)