# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 18:08:34 2020

@author: ChangYeol
"""
# N과 M 1
# https://codedrive.tistory.com/194

N,M = map(int,input().split())

num_list = [i for i in range(1,N+1)]
check_list = [False]*N

arr = []

# 주어진 개수가 채워지면 출력된다.
def dfs(cnt):
    # 갯수가 찬 경우 arr을 출력하고 끝난다.
    # 아래 for에서 마지막 순환 때 cnt+1이 되어 for반복수만큼 dfs가 다시 호출된다.
    # 그럼 그 반복수만큼 이 부분이 실행되게 되는 것이다.
    if cnt==M:
        print(*arr)
        return

    for i in range(N):
        # 이미 나온 값은 거른다.
        if check_list[i]:
            continue

        # 나올 수 리스트들에 대한 for이기 때문에 i는 첫번째 노드가 된다.
        # 그래서 등장한 것으로 추가하고 num_list를 추가한다.
        check_list[i] = True
        arr.append(num_list[i])

        # 다음번째로 골라질 숫자
        dfs(cnt+1)

        # 리스트를 계속 사용하기 위해 위의 재귀가 호출되고 나면 한 자리를 pop시킨다.
        # pop시켰으므로 false로 만들어준다.
        arr.pop()
        check_list[i] = False

# 호출할 때의 인자는 재귀함수에서 현재 몇 자리를 찾았는지 확인할 때 사용한다.
dfs(0)


# 1
def sequence(stack,numbers,M):
    if len(stack)==M:
        print(*stack)
        return
    else:
        for number in numbers:
            if not number in stack:
                stack.append(number)
                sequence(stack,numbers,M)
                stack.pop()
 
a,b=map(int,input().split())
numbers=list(range(1,a+1))
stack=[]
for number in numbers:
    if not number in stack:
        stack.append(number)
        sequence(stack,numbers,b)
        stack.pop()
        
        

# 2
        
def go(N, M, count, line, excludes):
	global arr
	if M == count:
		print(line)
	else:
		if count == 0:
			for i in range(N):
				if i not in excludes:
					go(N, M, count+1, str(arr[i]), excludes + (i, ))
		else:
			for i in range(N):
				if i not in excludes:
					go(N, M, count+1, line + " " + str(arr[i]), excludes + (i, ))

N, M = map(int, input().split(" "))

arr = list(range(1, N+1))

go(N, M, 0, "", ())


# 3
def npr(n, k, N):
    if n == k:
        print(' '.join(map(str, p)))
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                p[n] = i+1
                npr(n+1, k, N)
                used[i] = 0

N, M = map(int, input().split())
used = [0] * N
p = [0] * M
npr(0, M, N)

# N과 M 2
# https://wlstyql.tistory.com/58?category=852442
N, M = map(int, input().split())
visited = [False] * N
out, out_all = [], []

def solve(depth, N, M):
    if depth == M:
        out_str = ' '.join(map(str, sorted(out)))
        if out_str not in out_all:
            out_all.append(out_str)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            solve(depth+1, N, M)
            visited[i] = False
            out.pop()
solve(0, N, M)

for i in out_all:
    print(i)


# N과 M 3
N, M = map(int, input().split())
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(N):
        out.append(i+1)
        solve(depth+1, N, M)
        out.pop()

solve(0, N, M)
    

# N과 M 4
def f(n,m,k,l):
    if(n == k):
        print(*res)
        return
    else:
        for i in range(m):
            if(arr[i] >= l):
                visited[i] = 1
                l = arr[i]
                res[n] = arr[i]
                f(n+1,m,k,l)
                visited[i] = 0

n, m = map(int, input().split())
arr = range(1,n+1)
visited = [0 for i in range(n)]
res = [0] * m
f(0,n,m,0)
