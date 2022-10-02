from sys import stdin

t = int(input())

for _ in range(t):
    h, w, n = map(int, stdin.readline().strip().split())
    remainder = n % h
    if remainder:
        tmp = '0' + str((n // h) + 1)
        print(tmp, remainder)
        print(str(remainder) + tmp[-2:])
    else:
        tmp = '0' + str(h)
        print(str(n // h) + tmp[-2:])