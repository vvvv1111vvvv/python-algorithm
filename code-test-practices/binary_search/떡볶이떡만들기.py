def sum(cut):
    total=0
    for data in array1:
        if data>cut:
            total+=data-cut
    return total
def binarySearch(array, target, start, end):
    temp_result=0
    while start<=end:
        mid=(start+end)//2
        if sum(mid)==target:
            return mid
        elif  sum(mid)<target:
            end=mid-1
        elif sum(mid)>target:
            start=mid+1
            temp_result=mid
    return temp_result
n, m= map(int, input().split())
array1=list(map(int, input().split()))
print(binarySearch(array1, m, 0, max(array1)))