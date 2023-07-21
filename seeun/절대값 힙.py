# 우선순위 큐 사용
from queue import PriorityQueue
import sys
input = sys.stdin.readline
N = int(input())
arr = PriorityQueue() #우선순위 큐 : 자동으로 정렬된다

for _ in range(N):
    num = int(input()) # 정수 투입
    if num == 0: # 정수 = 0
        if arr.empty(): #배열이 비어있을 경우
            print('0') #0 출력
        else: #배열이 비어있지 않다면
            print(str(arr.get()[1])) #가장 작은 값 출력 #절대값이 아닌 값을 출력해야하므로 [1]
    else: # 정수 != 0
        arr.put((abs(num), num)) # 정렬 기준을 절대값 > 숫자 순으로 설정