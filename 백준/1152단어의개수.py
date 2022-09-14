from collections import Counter
from sys import stdin

input = stdin.readline
n = int(input())
num = sorted([int(input()) for _ in range(n)])

print(round(sum(num)/len(num))) # 평균
print(num[n//2]) # 중앙값
tmp = Counter(num)
tmp = tmp.items()
tmp = sorted(tmp, key=lambda x: (-x[1], x[0]))
if n == 1 or tmp[0][1] > tmp[1][1]:
    print(tmp[0][0])
else:
    print(tmp[1][0])
print(max(num) - min(num)) # 범위