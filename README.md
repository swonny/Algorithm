# Algorithm

## basic-algorithm

### branch1.py
연산자 종류
1. 단항 연산자 : 피연산자 1개
    - ex. -a
2. 이항 연산자
    - ex. a < b
3. 삼항 연산자
    - ex. a if b else c

### range()
- 이터러블 객체 생성
```python
range(n) # 0 이상 n 미만인 수를 나열하는 수열 생
range(a, b) # a 이상 b 미만인 수를 차례로 나열하는 수열
range(a, b, step) # a 이상 b 미만인 수를 step 간격으로 나열하는 수열
```

### 이터러블
- 반복할 수 있는 객체로, for~in 문에 사용할 수 있다.
- 이터러블 자료형 : list, str, tuple


### 튜플


### 언더스코어(_)
- 파이썬에서는 무시하고 싶은 값을 언더스코어로 표현할 수 있다.

### 🔴 basic-algorithm / print_stars1.py

### reactangle.py
- 🔴 (이유) 넓이가 ```area```인 사각형은 ```i * i > area```인 첫 번째 i를 가장 긴 변으로 가질 수 있다. 
- for문이나 while문의 끝부분에는 다음과 같이 else문을 둘 수 있다.
```python
for i in range(1, 10):
    r = random.randint(10, 99) # 두 자리수의 난수 생성
    if r == 13: break
else:
    print('for문 뒤에는 else문을 둘 수 있습니다.')
```
위와 같이 for문이 10번 반복되어 조건식에 의해 반복문이 종료되는 경우 이 else문을 실행한다. <br/>
이때 r이 13일 때는 강제종료되어 else문을 수행하지 않은 채 for문을 빠져나온다.

### multiplication_table.py
- ```i*j:3``` 은 i*j를 세자리수로 나타낸 것이다.

### 난수 생성
```python
import random

random.randint(start, end) # start부터 end 사이 정수 중 무작위 1개를 반환한다.
```