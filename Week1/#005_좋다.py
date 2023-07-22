#005
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
array = list(map(int, input().split()))

d = [0]*n
r = [0]*m

d[0] = array[0]
answer = 0

for i in range(1,n):
    d[i] = d[i-1] + array[i]

for i in range(n):
    remainder = d[i]%m
    if remainder == 0 :
        answer += 1
    r[remainder] += 1

for i in range(m):
    if r[i] > 1:
        answer += (r[i]*(r[i]-1) // 2)

print(answer)