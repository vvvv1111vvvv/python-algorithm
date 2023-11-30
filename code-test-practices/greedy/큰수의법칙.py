#N, M, K를 입력받기
n, m, k = map(int, input().split(" "))
#데이터를 공백으로 구분하여 입력받기
data = list(map(int, input().split(" ")))
#데이터 정렬
data.sort()
first = data[n - 1]
second = data[n - 2]
result = 0
var = 0
for i in range(0, m):
  if i == 0:
    var = first
  elif i % k == 0:
    var = second
  else:
    var = first
  result += var
print(result)
