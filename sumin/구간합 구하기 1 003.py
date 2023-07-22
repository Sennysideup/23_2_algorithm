import sys
input = sys.stdin.readline

# 입력값 받기
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 합 배열 sum 정의
p_sum = [0] * (N + 1)
for k in range(1, N + 1):
	p_sum[k] = p_sum[k-1] + numbers[k-1]

# S[j] - S[i-1] = i부터 j까지 합
n = 0
for n in range(M):
	i, j = map(int, input().split())
	total_sum = p_sum[j] - p_sum[i-1]
	print(total_sum)