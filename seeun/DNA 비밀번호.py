# DNA 비밀번호
# 교재 정답 입력 시 틀렸다고 나옴
# first try : 메모리 초과
from collections import Counter, deque

S, P = map(int, input().split()) # S : 전체 문자열 길이, P : 비밀번호 길이
DNA = input()
A, C, G, T = list(map(int, input().split())) # ACGT의 최소 개수
count = 0
answer = deque()

for i in range(S): #슬라이딩 윈도우 저장
    if len(DNA[i:i+P].strip()) == P: #i부터 end까지 들어가 있는 문자 개수 : P개
        answer.append(DNA[i:i+P].strip())
    else:
        break

for i in answer: #슬라이딩 윈도우 안의 문자열 count 및 비교
    if (A >= Counter(i)['A']) and (C >= Counter(i)['C']) and (G >= Counter(i)['G']) and (T >= Counter(i)['T']):
        count += 1
print(count)


### 해결 : Counter 모듈 대신 직접 dict 계산, 슬라이딩 윈도우 따로 저장X
S, P = map(int, input().split()) # S : 전체 문자열 길이, P : 비밀번호 길이
DNA = str(input()).strip()
A, C, G, T = list(map(int, input().split())) # ACGT의 최소 개수
dic = {'A':A, 'C':C, 'G':G, 'T':T}
base = {'A':0, 'C':0, 'G':0, 'T':0}

count = 0
for i in range(S-P+1):
    flag = True
    if i == 0:
        for j in range(P): #첫 번째 슬라이딩 윈도우에서
            base[DNA[j]] += 1 #각 문자에 해당하는 경우 +1
    else: # 두 번째 슬라이딩 윈도우부터는
        base[DNA[i+P-1]] += 1 # 추가된 문자에 해당하는 경우 +1
        base[DNA[i-1]] -= 1 # 삭제된 문자에 해당하는 경우 -1
    for i in ('A', 'G', 'C', 'T'):
        if base[i] < dic[i]: #현재 슬라이딩 윈도우와 정답값 비교
            flag = False
            break
    if flag:
        count += 1

print(count)