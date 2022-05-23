n = float(input())
denominator = 1
s = 0
while denominator <= n:
    num = 1 / denominator
    s += num
    denominator += 1
print(f'{s:2.4f}')
