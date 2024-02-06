'''
import bisect
n, x = map(int,input().split())
array=list(map(int, input().split()))
l=bisect.bisect_left(array,x)
r=bisect.bisect_right(array,x)
if r-l==0:
    print(-1)
else: 
    print(r-l)
'''