n= int(input())
array1=list(map(int, input().split()))
array1= sorted(array1)
m= int(input())
array2=list(map(int, input().split()))

#이진탐색
def binarySearch(array, target, start, end):
    if start>end:
        return "no"
    mid=(start+end)//2
    if array[mid]==target:
        return "yes"
    elif array[mid]>target:
        return binarySearch(array, target, start, mid-1)
    else:
        return binarySearch(array, target, mid+1, end)
for target in array2:
    print(binarySearch(array1, target, 0, n-1), end=" ")