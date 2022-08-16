from collections import deque
from sys import stdin

queue = deque([])

N = stdin.readline().rstrip()

for _ in range(int(N)):
    tmp = stdin.readline().rstrip()
    try:
        com, val = tmp.split()
    except ValueError:
        com = tmp
    
    if com == 'push_front':
        queue.appendleft(val)
        
    elif com == 'push_back':
        queue.append(val)
    
    elif com == 'pop_front':
        try:
            print(queue.popleft())
        except IndexError:
            print(-1)
            
    elif com == 'pop_back':
        try:
            print(queue.pop())
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
 