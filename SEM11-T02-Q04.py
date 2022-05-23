n = int(input())
if n == 2 or (n != 1 and n % 2 == 1):
    e_primo = True
else:
    e_primo = False
divisor = 3
while divisor < n // 2 and e_primo:
    if n % divisor == 0:
        e_primo = False
    divisor += 2

if e_primo:
    print(True)
else:
    print(False)
