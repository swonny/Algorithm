N = str(input())
tmp = list(map(str, '0' + N))
cnt = 0
n = len(tmp)
print(int(tmp[n - 2] + tmp[n - 1]))
while cnt < 3:
    cnt += 1
    n = len(tmp)
    print(int(tmp[n - 1]) + int(tmp[n - 2]))