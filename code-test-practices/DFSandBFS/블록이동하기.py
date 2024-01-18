from collections import deque
def bfs(board):
    n=len(board)
    count=0
    visited_horizental=[[False]*(n-1) for _ in range(n)]#기준 좌측 끝좌표
    visited_vertical=[[False]*(n) for _ in range(n-1)]#기준: 상단 끝좌표
    q=deque()
    q.append([(0,0),(0,1),0]) #0: horizen, #1:vertical
    visited_horizental[0][0]=True
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    now_vetical_upper_turn_dx=[-1,-1]
    now_vetical_upper_turn_dy=[-1,1]
    now_vetical_lower_turn_dx=[1,1]
    now_vetical_lower_turn_dy=[-1,1]
    
    now_horizental_upper_turn_dx=[-1,1]
    now_horizental_upper_turn_dy=[-1,-1]
    now_horizental_lower_turn_dx=[-1,1]
    now_horizental_lower_turn_dy=[1,1]
    
    now_direction_u_dx= [now_vetical_upper_turn_dx,now_horizental_upper_turn_dx]
    now_direction_u_dy= [now_vetical_upper_turn_dy,now_horizental_upper_turn_dy]
    now_direction_l_dx= [now_vetical_lower_turn_dx,now_horizental_lower_turn_dx]
    now_direction_l_dy= [now_vetical_lower_turn_dy,now_horizental_lower_turn_dy]
    while q:
        sz=len(q)
        for _ in range(sz):
            now=q.popleft()
            for i in range(4):
                nx1=now[0][0]+dx[i]
                nx2=now[1][0]+dx[i]
                ny1=now[0][1]+dy[i]
                ny2=now[1][1]+dy[i]
                if nx1<0 or nx2<0 or ny1<0 or ny2<0 or nx1>=n or nx2>=n or ny1>=n or ny2>=n:
                    continue
                if board[nx1][ny1]==1 or board[nx2][ny2]==1:
                    continue
                if now[2]==0:
                    if visited_horizental[nx1][ny1]==True:
                        continue
                elif now[2]==1:
                    if visited_vertical[nx1][ny1]==True:
                        continue
                q.append([(nx1,ny1),(nx2,ny2),now[2]])
                if now[2]==0:
                    visited_horizental[nx1][ny1]=True
                elif now[2]==1:
                    visited_vertical[nx1][ny1]=True
                if (nx1,ny1) == (n-1,n-1) or    (nx2,ny2) == (n-1,n-1):
                    return count+1
            k=now[2]
            for i in range(4):
                if i==0:
                    nx1=now[0][0]
                    nx2=now[1][0]+now_direction_u_dx[k][i]
                    ny1=now[0][1]
                    ny2=now[1][1]+now_direction_u_dy[k][i]
                elif i==1:
                    nx1=now[0][0]+now_direction_u_dx[k][i]
                    nx2=now[1][0]
                    ny1=now[0][1]+now_direction_u_dy[k][i]
                    ny2=now[1][1]
                elif i==2:
                    nx1=now[0][0]
                    nx2=now[1][0]+now_direction_l_dx[k][i-2]
                    ny1=now[0][1]
                    ny2=now[1][1]+now_direction_l_dy[k][i-2]
                elif i==3:
                    nx1=now[0][0]+now_direction_l_dx[k][i-2]
                    nx2=now[1][0]
                    ny1=now[0][1]+now_direction_l_dy[k][i-2]
                    ny2=now[1][1]
                if nx1<0 or nx2<0 or ny1<0 or ny2<0 or nx1>=n or nx2>=n or ny1>=n or ny2>=n:
                    continue
                if board[nx1][ny1]==1 or board[nx2][ny2]==1:
                    continue
                if k==0:
                    if i==0:
                        diagonal_point_x=nx2
                        diagonal_point_y=ny2+1
                    elif i==1:
                        diagonal_point_x=nx1
                        diagonal_point_y=ny1-1
                    elif i==2:
                        diagonal_point_x=nx2
                        diagonal_point_y=ny2+1
                    elif i==3:
                        diagonal_point_x=nx1
                        diagonal_point_y=ny1-1
                elif k==1:
                    if i==0:
                        diagonal_point_x=nx2+1
                        diagonal_point_y=ny2
                    elif i==1:
                        diagonal_point_x=nx1-1
                        diagonal_point_y=ny1
                    elif i==2:
                        diagonal_point_x=nx2+1
                        diagonal_point_y=ny2
                    elif i==3:
                        diagonal_point_x=nx1-1
                        diagonal_point_y=ny1
                
                if board[diagonal_point_x][diagonal_point_y]==1:
                    continue
                calc=sorted([(nx1,ny1),(nx2,ny2)], key= lambda x: (x[0],x[1]))
                if now[2]==0:
                    if visited_vertical[calc[0][0]][calc[0][1]]==True:
                        continue
                    visited_vertical[calc[0][0]][calc[0][1]]=True
                elif now[2]==1:
                    if visited_horizental[calc[0][0]][calc[0][1]]==True:
                        continue
                    visited_horizental[calc[0][0]][calc[0][1]]=True
                temp=[]
                for val in calc:
                    temp.append(val)
                temp.append(0 if now[2]==1 else 1)
                q.append(temp)
                if (nx1,ny1) == (n-1,n-1) or    (nx2,ny2) == (n-1,n-1):
                    return count+1
            
        count+=1      


def solution(board):
    
    answer = bfs(board)
    
    return answer
print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))