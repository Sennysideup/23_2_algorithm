from collections import deque
N = int(input())
card = deque()

# 수열 생성
for i in range(1, N+1):
    card.append(i)

while len(card) > 1: #카드가 한 장 남을 때까지
    card.popleft() # 가장 앞에 있는 데이터 삭제
    card.append(card[0]) #앞에 있는 데이터 이동
    card.popleft() # 이동시킨 데이터 원본 삭제

print(card[0]) #정답률 50%로 평이한 난이도