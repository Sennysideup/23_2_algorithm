N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
S = sum(scores)
answer = S / M * 100 / N
print(answer)