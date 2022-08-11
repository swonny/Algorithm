from copy import deepcopy
from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

stk = [] # 크기 비교 스택
res = [] # 결과 저장 스택 : 출력 시 뒤집어야 함
tmp = [] # 크기 비교시 임시 저장 스택

idx = -1
while True:
    if -idx > len(arr):
        break
    else:
        top = len(stk)
        if top == 0:
            res.append(-1)
            stk.append(arr[idx])
            idx -= 1
            continue
        if stk[top - 1] > arr[idx]:
            res.append(stk[top - 1])
            stk.append(arr[idx])
        else:
            tmp.append(stk.pop())
            continue
        # if len(tmp) > 0:
        #     tmp.reverse()
        #     # for n in tmp:
        #     #     stk.append(n)
        #     new = stk + tmp
        #     print(new)
        #     tmp.clear()
        idx -= 1

res.reverse()        
print(' '.join(map(str, res)))