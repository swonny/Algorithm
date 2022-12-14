# Algorithm

# 🗓 계획

|완료|날짜|단원|백준|인덱스|
|:--:|:--:|:--:|:--:|:--:|
|✓|08.03|02장|단계별문제:배열|[Datastructure_Array](#02datastructurearray)|
|✓|08.04 ~ 08.06|03장|-|[검색](#03검색)|
|✓|08.07 ~ 08.09|04장|단계별문제:스택, 큐와덱|[스택과큐](#04스택과큐)|
|✓|08.10 ~ 08.12|05장|-|🔴하노이의 탑, 8퀸 문제 이해 필요|
|✓|08.15 ~ 08.22|06장|-|🔴이슈 확인 필요|
|✓|08.23 ~ 08.25|07장|-|🔴 KMP, 보이어 무어법 이해 필요|
|✓|08.26 ~ 08.28|08장|-|-|
|✓|08.29 ~ 08.31|09장|-|🔴 코드 직접 구현해보기|

**완료 기준 : 이틀 이상 고민해봤는데도 모르는 문제를 제외하고 한 챕터를 모두 이해했는지**
***

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
이때 r이 13일 때는 강제종료되어 else문을 수행하지 않은 채 for문을 빠져나온다.<br/>

### multiplication_table.py
- ```i*j:3``` 은 i*j를 세자리수로 나타낸 것이다.

### 난수 생성
```python
import random

random.randint(start, end) # start부터 end 사이 정수 중 무작위 1개를 반환한다.
```

### 파이썬의 변수명
파이썬은 모든 함수, 클래스, 데이터, 모듈, 패키지 등을 모두 객체로 취급한다. 객체는 자료형을 가지며 메모리를 차지한다. 따라서 파이썬의 변수는 값을 갖지 않는다.<br/>
--> ```n = 17``` 과 같이 n이라는 변수에 17을 대입했을 때 n에 17의 값이 대입되는 것이 아니라 17이라는 객체를 n이라는 변수가 참조하는 것일 뿐이다.<br/>

### 리스트와 튜플
- 리스트
    - 원소를 변경할 수 있는 ```mutable```객체이다.<br/>
    - list()를 사용하여 다양한 객체를 원소로 하는 리스트를 생성할 수 있다.<br/>
    - 리스트의 원소 개수는 리스트를 만들기 전에 반드시 결정해야 한다. <br/>
      하지만 원솟값을 정하지 않으면서 원소의 개수를 정하는 리스트는 ```list01 = [None] * 5```와 같이 나타낼 수 있다.<br/>

- 튜플<br/>
    - 튜플은 원소를 변경할 수 없는 ```immutable```객체이다.<br/>
    - 튜플을 생성할 때는 결합 연산자 ()를 생략하여 ```tuple1 = 1,```와 같이 나타낼 수 있다.<br/>

# 📁 Directories

#  02.Datastructure_Array
- 리스트, 배열과 관련하여 설명이 필요한 부분이 많아 주피터 노트북으로 저장<br/>
    🔴 배열.jpynb > 소수 구하기 프로그램 > 소수 구하기 프로그램 <개선2><br/>
        : 직사각형 넓이 & 짧은 변의 길이 중 가장 긴 변의 길이 구하는 부분 이해 못함<br/>
    
    🟢 (해결) 백준 > 1차원배열 > 4344 평균은 넘겠지 해결 필요<br/>

# 03.검색
08.04 : 선형검색<br/>
08.05 : 이진검색, 해시법(체인법까지)<br/>
08.08 : 해시법(오픈 주소법까지)<br/>

# 04.스택과큐
08.08 : 스택<br/>
08.09 : 큐<br/>
🟢 (해결) 큐 > 링 버퍼의 활용<br/>
    - 링 버퍼의 인덱스의 시작이 왜 (cnt - n)부터인지 생각이 잘 정리되지 않음. 인덱스가 0부터인 것과도 관련이 있나?<br/>
    - 04.스택과 큐 > 큐 > 링 버퍼 인덱스에 대하여 참고<br/>

# 05. 재귀 알고리즘
08.10 : 소단원 1, 2 재귀 알고리즘과 스택을 이용한 비재귀적 구현 완성<br/>
    - 🔴 유클리드 호제법<br/>
08.11 : 소단원 3, 4 하노이의 탑, 8퀸<br/>
08.12 : <br/>
    - 🔴 하노이의 탑 구현은 성공.. 이해 필요<br/>
    - 🔴 8퀸은 다시 처음부터 <br/>
    - 🔴 백준 > 재귀 > 2447 별찍기-10 : 3일 동안 고민하다가 다른 사람의 코드를 참고하였다.[출처](https://cotak.tistory.com/38) 다시 짜보자!<br/>

# 06. 정렬
08.15 : 버블 정렬, 선택 정렬, 삽입 정렬까지 <br/>
    - 🟢 (해결) 이진 삽입 정렬 다시 하기<br/>
08.16 : 셸 정렬 <br/>
08.17 : 백준 - AC 문제 해결<br/>
08.18 : 버블 정렬 직접 코드 짜기 완성<br/>
        ```직접 코드를 짜면 내 논리의 오류와 개선해야 하는 부분이 눈에 보이고, 더 효율적인 코드를 짤 수 있게 된다!```<br/>
08.19 : 선택 정렬, 삽입 정렬<br/>
    - 🔴 셸 정렬 이해 필요<br/>
08.22 : 정렬 완료 예정<br/>
    - 🔴 퀵 정렬 이해 필요<br/>
08.23 : ~ 힙 정렬 완료, 단계별 반복문, 조건문 완성<br/>
    - 🔴 도수 정렬 구현 필요<br/>

# 07. 문자열 검색
08.24 : 브루트 포스법 완료<br/>

# 09. 트리
08.25 : 트리 (이진검색트리 삭제 구현 전까지 완료)<br/>

# 08. 리스트
08.26 : 08장 2챕터 포인터를 이용한 연결리스트 구현 완료

