def check_wall(map1, snake):
    if snake[0][0]>=len(map1) or snake[0][1]>=len(map1) or snake[0][0]<0 or snake[0][1]<0: 
        return True
def check_self_construction(map1, snake):
    if [snake[0][0],snake[0][1],0] in snake[1:] or [snake[0][0],snake[0][1],1] in snake[1:] or [snake[0][0],snake[0][1],2] in snake[1:] or[snake[0][0],snake[0][1],3] in snake[1:]:
        return True
def change_direction(snake_head, direction):
    if direction=='D': 
        snake_head[2]=snake_head[2]+1 if snake_head[2]<3 else 0        
    else:
        snake_head[2]=snake_head[2]-1 if snake_head[2]>0 else 3
    return snake_head
def move_step(map1, snake):
    if snake[0][2]==0:
        snake.insert(0,[snake[0][0],snake[0][1]+1,snake[0][2]])
    elif snake[0][2]==1:
        snake.insert(0,[snake[0][0]+1,snake[0][1],snake[0][2]])
    elif snake[0][2]==2:
        snake.insert(0,[snake[0][0],snake[0][1]-1,snake[0][2]])
    elif snake[0][2]==3:
        snake.insert(0,[snake[0][0]-1,snake[0][1],snake[0][2]])
    if check_wall(map1, snake)==True or check_self_construction(map1, snake)==True:
        return map1, snake, True    
    if map1[snake[0][0]][snake[0][1]]==1:
        map1[snake[0][0]][snake[0][1]]=0
    else:
        snake.pop()
    return map1, snake, False

n=int(input())
k=int(input())
map1=[[0]*n  for _ in range(n)]
for _ in range(k):
    x,y= map(int,input().split())
    map1[x-1][y-1]=1
l=int(input())
move=[]
for _ in range(l):
    temp=input().split()
    temp[0]=int(temp[0])
    move.append(temp)
snake_head=[0,0,0]
snake=[snake_head]
count=0
time, direction=move.pop(0)
while count<10001:
    map1, snake, flag=move_step(map1, snake)
    count+=1
    if flag== True:
        break
    if count==time:
        snake.insert(0,change_direction(snake.pop(0), direction))
        if len(move)!=0:
            time, direction=move.pop(0)
print(count)