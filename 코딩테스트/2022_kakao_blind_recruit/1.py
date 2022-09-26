def transfer(n, k):
    res = []
    while n > 0:
        res.append(n % k)
        n //= k
    res.reverse()
    return res

def findPattern(res):
    zero = [0]
    for i in range(len(res)):
        if not res[i]:
            zero.append(i)
    zero.append(len(res))

    tmp = []
    for i in range(len(zero) - 1):
        tmp.append(res[zero[i]:zero[i+1]])
    
    for i, t in enumerate(tmp):
        tmp[i] = int(''.join(map(str, t)))
    return tmp

def getPrime(tmp):
    cnt = 0
    for t in tmp:
        flag = False
        if t > 1:
            for i in range(2, int(t**(1/2))+1):
                if t % i == 0:
                    flag = True
                    break
            cnt += 1 if not flag else 0
    return cnt
        
n, k = map(int, input().split())
res = transfer(n, k)
# print(res)
tmp = findPattern(res)
print(tmp)
print(getPrime(tmp))



