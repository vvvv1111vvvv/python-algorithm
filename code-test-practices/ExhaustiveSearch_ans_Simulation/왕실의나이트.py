# 입력을 받는 부분
input_datas=input()

x=int(ord(input_datas[0]))-int(ord('a'))+1
y=int(input_datas[1])
count=0
result=[]

dx=[1,2,2,1,-1,-2,-2,-1]
dy=[-2,-1,1,2,2,1,-1,-2]
move_types=['UR','RU','RD', 'DR', 'DL', 'LD','LU','UL']

for i in range(len(move_types)):
    nx=x+dx[i]
    ny=y+dy[i]
    if(nx<1 or nx>8 or ny<1 or ny>8):
        continue
    count+=1
    temp=nx+ord('a')-1
    result.append(chr(temp)+str(ny))
print(count)
print(result)

