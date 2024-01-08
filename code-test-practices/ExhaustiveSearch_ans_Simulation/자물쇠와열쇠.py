import copy
def turn(key):
    #90도 회전
    turnedKey=[[0]*len(key) for _ in range(len(key[0]))]
    for row in range(len(key)):
        for column in range(len(key[0])):
            turnedKey[column][len(key)-row-1]=key[row][column]
    return turnedKey
def check(map,key,lock):
    for row in range(len(key),len(key)+len(lock)):
        for column in range(len(key),len(key)+len(lock)):
            if map[row][column]!=1:
                return False
    return True
def add_map_lock(key,  lock):
    map=[[0]*(len(key)*2+len(lock)) for _ in range(len(key)*2+len(lock))]
    for row in range(len(lock)):
        for column in range(len(lock)):
            map[len(key)+row][len(key)+column]=lock[row][column]
    return map
def calcul(key, lock,origin_map):
    for x in range(1,len(key)+len(lock)):
        for y in range(1,len(key)+len(lock)):
            map=copy.deepcopy(origin_map)
            for x1 in range(len(key)):
                for y1 in range(len(key)):
                    map[x+x1][y+y1]+=key[x1][y1]
            if check(map,key,lock)==True:
                return True
            
    return False
                
def solution(key, lock):
    #lock이 바로 통과되는 경우
    if lock==[[1]*len(lock) for _ in range(len(lock))]:
        return True
    
    origin_map= add_map_lock(key, lock)
    for _ in range(4):
        key = turn(key)
        if calcul(key,lock,origin_map)==True:
            return True
    return False
print(solution(	[[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))