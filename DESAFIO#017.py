import math
c1 = float(input('Digite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjacente: '))
hp = math.hypot(c1,c2)
print(f'A hipotenusa é: {hp:.2f}')