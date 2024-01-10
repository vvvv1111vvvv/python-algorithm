#https://school.programmers.co.kr/learn/courses/30/lessons/60062
from itertools import permutations
def solution(n, weak, dist):
    length=len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer=len(dist)+1
    for start in range(length):
        for friend in sorted(list(permutations(dist,len(dist))), reverse=True):
            #count= 투입한 친구 수
            count=1
            #position:해당 친구가 마지막으로 점검하는 위치
            position=weak[start]+friend[count-1]
            for index in range(start, start+length):
                if weak[index]>position:
                    count+=1
                    if count>len(dist):
                        break
                    position=weak[index]+friend[count-1]
            answer=min(answer, count)            
    if answer<len(dist)+1:
        return answer
    else:
        return -1
                
    