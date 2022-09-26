n, k = map(int, input().split())
l = []
for i in range(1, n + 1):
    if n % i == 0:
        l.append(n//i)
l = sorted(list(set(l)))
print(0 if len(l) < k else l[(k-1)])

# 1 2 5 10