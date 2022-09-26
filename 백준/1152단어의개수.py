from sys import stdin

input = stdin.readline
n = int(input())
num = dict()
for _ in range(n):
    key = int(input())
    if key in num:
        num[key] += 1
    else:
        num[key] = 1
num = sorted(num.items())
for (n, c) in num:
    print((str(n) + '\n') * c, end='')