N=int(input())
data= list(map(str, input().split(" ")))
resulta=1
resultb=1

for i in data:
    if(i=='R'and resultb<N):
        resultb+=1
    elif(i=='L'and resultb>1):
        resultb-=1
    elif(i=='U' and  resulta>1):
        resulta-=1
    elif(i=='D' and resulta<N):
        resulta+=1
print(resulta, resultb)