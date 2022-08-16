from collections import deque
from sys import stdin

queue = deque([])

N = stdin.readline().rstrip()

for _ in range(int(N)):
    tmp = stdin.readline()
    try:
        com, val = tmp.split()
    except ValueError:
        com = tmp
    
    if com == 'push':
        queue.append(val)
    
    elif com == 'pop':
        try:
            print(queue.popleft())
        except IndexError:
            print(-1)
    
    elif com == 'size':
        print(len(queue))
    
    elif com == 'empty':
        if not queue:
            print(1)
            continue
        print(0)
    
    elif com == 'front':
        if not queue:
            print(-1)
            continue
        print(queue[0])
    
    elif com == 'back':
        if not queue:
            print(-1)
            continue
        print(queue[len(queue) - 1])
        