# 버블 정렬 알고리즘 개선 2 - 내가 짠 코드

def bubble_sort2(arr):
    n = len(arr)
    cnt = 0
    i = 0
    while i < n:
        last = n - 1
        cnt += 1
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                last = j - 1
                print('test')
        print(last)
        i = last + 1
    
    print(f'array : {a}, cnt: {cnt}')

a = [1, 3, 9, 2, 4]
bubble_sort2(arr)
print(a)