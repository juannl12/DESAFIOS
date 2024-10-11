n1 = int(input('Digite um número de 0 a 9999: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 100 % 1
print(f'Seu número é: {n1}')
print(f'A Unidade é:  {u}')
print(f'A Dezena é:  {d}')
print(f'A Centena é:  {c}')
print(f'A Milhar é:  {m}')