def max3(a, b, c):
    max = a
    if b > max : max = b
    if c > max : max = c
    return max


print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')
print(f'max3(2, 1, 4) = {max3(2, 1, 4)}')