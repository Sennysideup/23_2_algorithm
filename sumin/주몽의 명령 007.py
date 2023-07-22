import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
nums = list(map(int, input().split()))
nums.sort()
count = 0
i = 0  #start_index
j = N-1  #end_index

while i < j:
    if nums[i] + nums[j] == M:
        count += 1
        j -= 1
        i += 1
    elif nums[i] + nums[j] > M:
        j -= 1
    else:
        i += 1

print(count)

