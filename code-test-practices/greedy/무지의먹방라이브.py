def solution(food_times, k):
    if k>=sum(food_times):
        return -1
    i=0
    for _ in range(k+1):
        i%=len(food_times)
        while food_times[i]<1:
            i=(i+1)%len(food_times)
        food_times[i]-=1
        i+=1
    return i