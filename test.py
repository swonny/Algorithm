# 개선 코드

from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

stk = [] # 크기 비교 스택
res = [] # 결과 저장 스택 : 출력 시 뒤집어야 함

idx = -1
while -idx <= len(arr):
    if not stk:
        res.append(-1)
    else:
        if stk[-1] > arr[idx]:
            res.append(stk[-1])
        else:
            stk.pop()
            continue
    stk.append(arr[idx])
    idx -= 1

res.reverse()        
print(' '.join(map(str, res)))