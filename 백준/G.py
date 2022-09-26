n, k = map(int, input().split())
score = list(map(int, input().split()))
group = []
i = 0
d = n // k
while i < n:
    group.append(sum(score[i:i+d]))
    i += d

print(min(group))