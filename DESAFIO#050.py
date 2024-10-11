from time import sleep
s = 0
for c in range(0,8, 2):
    print(c)
    sleep(0.7)
    if c % 2 == 0:
        s = s + c
print(f'A soma do dos números acima é {s}')
