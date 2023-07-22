#변수 선언
N = int(input())
count = 1 #자기 자신 경우 포함
start_index = 1
end_index = 1
sum = 1

#투포인터
while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index +=1
        sum += end_index

print(count)