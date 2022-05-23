n_termo = int(input())
num1, num2 = 0, 1
contador = 0
while contador < n_termo:
    print('{}, '.format(num1), end='')
    num1, num2 = num2, num1 + num2
    contador += 1
