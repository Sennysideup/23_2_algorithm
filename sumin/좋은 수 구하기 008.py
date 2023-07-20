import sys
input = sys.stdin.readline

# 입력 받기 및 변수 선언
N = int(input())
A = list(map(int, input().split()))
count = 0
A.sort() #투포인터 위해 오름차순 정렬

#A 리스트 순회
for i in range(N):
    K = A[i]
    k = 0 #start_index
    j = N - 1 #end_index
    #투포인터
    while k < j:
        if A[k] + A[j] == K:
            if k != K and j != K: #서로 다른 수 정답
                count += 1
                break
            elif k == K:
                k += 1
            elif j == K:
                j-=1
        elif A[k] + A[j] < K:
            k += 1
        else:
            j -= 1

print(count)

