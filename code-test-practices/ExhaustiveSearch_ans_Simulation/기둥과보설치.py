#https://school.programmers.co.kr/learn/courses/30/lessons/60061]\
def possible(answer):
    for x,y,stuff in answer:
        if stuff==0:
            #기둥이면
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            else: 
                return False
        else:
            #보이면
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer=[]
    for value in build_frame:
        if value[3]==0: 
            answer.remove(value[:3])
            if possible(answer):
                continue
            answer.append(value[:3])
            
        else:
            answer.append(value[:3])
            if possible(answer):
                continue
            answer.remove(value[:3])
    answer.sort()
    return answer