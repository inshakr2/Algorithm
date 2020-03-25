# -*- coding: utf-8 -*-

# 동전 0

N, K = map(int, input().split()) 
value_list = [] 

for _ in range(N): 
    value = int(input()) 
    
    if value <= K: 
        value_list.append(value) 
        
cnt = 0 
for i in range(len(value_list)): 
    value = value_list[(len(value_list))-i-1] 
    cnt += (K // value) 
    K = K%value 
    
print(cnt)

# ATM

N = int(input())
nums = list(map(int, input().split()))

if N == 1 : #1
    print(nums[0])
else : 
    nums.sort() #2

    i_sum = 0 
    min_sum = 0

    for i in range(N): 
        min_sum += (i_sum + nums[i]) #3
        i_sum += nums[i] #4
        
    print(min_sum)
    
    
# 회의실 배정 

import sys

N = int(input())
meeting = []
for _ in range(N):
    meeting.append(list(map(int, sys.stdin.readline().split())))

meeting = sorted(meeting, key = lambda x: [x[1], x[0]])


#빨리 끝나는 것 중 가장 빨리 시작하는 순서대로 더해준다.
max_meeting = 0
start = 0
for meet in meeting:
    if meet[0] >= start:
        start = meet[1]
        max_meeting += 1
        
print(max_meeting)