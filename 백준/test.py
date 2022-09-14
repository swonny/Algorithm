from sys import stdin

N, S = map(int, input().split())
L = [int(stdin.readline()) for _ in range(N)]
cnt = 0
    
L.sort()
N = len(L)
flag = False
for i in range(N - 1):
    tmp = S - L[i]
    for j in range(i + 1, N):
        if L[j] > tmp:
            break
        cnt += 1
        flag = True
    if not flag:
        break
        
print(cnt)