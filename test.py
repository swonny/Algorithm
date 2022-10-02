from sys import stdin

# t = int(input())

h, w, t = map(int, stdin.readline().strip().split())
for n in range(1, h * w + 1):
    remainder = n % h
    if remainder:
        tmp = '0' + str((n // h) + 1)
        print(str(remainder) + tmp[-2:])
    else:
        tmp = '0' + str(n // h)
        print(str(h) + tmp[-2:])