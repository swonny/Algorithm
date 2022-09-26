def transfer(n, k):
    res = []
    while n > 0:
        res.append(n % k)
        n //= k
    res.reverse()
    return res

def findPattern(res):
    res = ''.join(map(str, res))
    tmp = list(map(int, filter(lambda x: x, res.split('0'))))
    return tmp

def getPrime(tmp):
    cnt = 0
    for t in tmp:
        flag = False
        if t > 1:
            for i in range(2, t):
                if t % i == 0:
                    flag = True
                    break
            cnt += 1 if not flag else 0
    return cnt
        
n, k = map(int, input().split())
res = transfer(n, k)
print(res)
tmp = findPattern(res)
print(tmp)
print(getPrime(tmp))



