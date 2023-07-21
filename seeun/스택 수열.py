## first try : 시간 초과
# stack은 제일 나중에 들어간 자료가 제일 먼저 나오는 특성
N = int(input()) #수열 개수
numbers = [int(input()) for _ in range(N)] #수열 채우기
stack = list()
num = 1
answer = ""

for i in range(N):
    su = numbers[i] # 현재 수열
    while su >= num: # 현재 수열 이하의 자연수에 대해서
        stack.append(num) #append
        num += 1 # 자연수 1 증가
        answer += "+\n" #정답값에 + 표시
    if stack == []: #수열을 만들 수 없는 경우
        answer = 'NO'
        break
    # 현재 수열 초과하는 자연수에 대해서
    elif stack[-1] == su: #
        stack.pop() # 현재 수열이 오름차순 자연수와 같다면 자연수 삭제
        answer += "-\n"
        
print(answer)

# answer
## 해결 : 반복문 안에서 input을 받는다
count = 1
temp = True
stack = []
op = []

N = int(input())
for i in range(N):
    num = int(input()) #반복문으로 여러 줄의 입력 받기
    while count <= num: #num 이하의 자연수를 스택에 추가
        stack.append(count)
        op.append('+')
        count += 1
    if stack[-1] == num: #마지막 stack 값이 num과 같으면 삭제
        stack.pop()
        op.append('-')
    else:
        temp = False
        break

if temp == False:
    print('NO')
else:
    for i in op:
        print(i)