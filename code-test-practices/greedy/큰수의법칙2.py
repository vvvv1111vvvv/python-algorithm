#N, M, K를 입력받기
n, m, k = map(int, input().split(" "))
#데이터를 공백으로 구분하여 입력받기
data = list(map(int, input().split(" ")))
#데이터 정렬
data.sort()
first = data[n - 1]
second = data[n - 2]
result = 0
#가장 큰수가 더해지는 회수
count=int(m/(k+1))*k+m%(k+1)
result=count*first+(m-count)*second
print(result)