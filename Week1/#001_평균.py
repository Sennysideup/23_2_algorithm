#001
import sys
input = sys.stdin.readline

n  = int(input())
score = list(map(int, input().split()))

score.sort(reverse=True)

score = [(i/score[0])*100 for i in score]

print(sum(score)/n)
