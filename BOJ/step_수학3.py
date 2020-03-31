# -*- coding: utf-8 -*-

# 배수와 약수

def solution(x,y) :
    if x % y == 0:
        return 'multiple'
    elif y % x == 0:
        return 'factor'
    else :
        return 'neither'

x, y = map(int,input().split(' '))

while x != 0 and y != 0:
    print(solution(x, y))
    
    x, y = map(int,input().split(' '))
    
# 약수

N = int(input())
gcd_list = list(map(int, input().split()))
gcd_list = sorted(gcd_list)
answer = 0

for i in range(len(gcd_list)):
    answer += gcd_list[i] * gcd_list[-i-1]

print(answer//len(gcd_list))


n = int(input())
a = list(map(int, input().split()))
a_max = max(a)
a_min = min(a)
print(a_max * a_min)



# 소인수분해

N = int(input())
i = 2

while N != 1:
    if N % i == 0:
        N = N/i
        print(i)
    else:
        i += 1
