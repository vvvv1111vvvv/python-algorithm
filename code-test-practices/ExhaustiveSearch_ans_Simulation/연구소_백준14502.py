import copy
from itertools import combinations
def spread_virous(data):
    virous_point=[]
    for row in range(len(data)):
        for column in range(len(data[0])):
            if data[row][column]==2:
                virous_point.append([row,column])
    while virous_point:
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        v_point=virous_point.pop()
        for i in range(4):
            nx=v_point[0]+dx[i]
            ny=v_point[1]+dy[i]
            if nx<0 or ny<0 or nx>=len(data) or ny>=len(data[0]):
                continue
            elif data[nx][ny]==0:
                data[nx][ny]=2
                virous_point.append([nx,ny])
    return check_safe_square_count(data)
def check_safe_square_count(data):
    result=0
    for row in range(len(data)):
        for column in range(len(data[0])):
            if data[row][column]==0:
                result+=1
    return result
def check_safe_sqare_loc(data):
    result=[]
    for row in range(len(data)):
        for column in range(len(data[0])):
            if data[row][column]==0:
                result.append([row,column])
    return result
n,m=map(int, input().split())
data=[]
result=0
for _ in range(n):
    data.append(list(map(int, input().split())))
for i in list(combinations(check_safe_sqare_loc(data),3)):
    for loc in i:
        data[loc[0]][loc[1]]=1
    result=max(result, spread_virous(copy.deepcopy(data)))
    for loc in i:
        data[loc[0]][loc[1]]=0
print(result)
