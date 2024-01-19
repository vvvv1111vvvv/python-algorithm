#https://school.programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    result=[0]*(N+1)
    answer=[]
    stages.sort()
    tot_visitor=len(stages)
    for i in range(1,N+1):
        if tot_visitor==0:
            result[i:]=(0,i)
            break       
        result[i]=(stages.count(i)/tot_visitor,i)
        tot_visitor-=stages.count(i) 
    now=result[1:]
    now.sort(key= lambda x: (-x[0],x[1]))
    for i in range(0,N):
        answer.append(now[i][1])
    return answer