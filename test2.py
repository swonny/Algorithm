n = int(input())

count = 0

count += (n // 5)
n %= 5
count += (n // 3)
n %= 3

print(-1 if n else count)