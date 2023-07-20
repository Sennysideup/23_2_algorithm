#004
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
array = [[0]*(n+1)] # 숫자 리스트
d = [[0]*(n+1) for i in range(n+1)] # 합 배열

for i in range(n):
    value = [0] + [int(x) for x in input().split()]
    array.append(value)

for i in range(1, n+1):
    for j in range(1, n+1):
        d[i][j] = d[i][j-1] + d[i-1][j] - d[i-1][j-1] + array[i][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = d[x2][y2] - d[x2-1][y2] - d[x2][y1-1] + d[x1-1][y1-1]
    print(answer)