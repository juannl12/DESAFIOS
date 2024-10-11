print('-='*20)
print('       Analizador de Triângulos       ')
print('-='*20)
r1 = float(input('Digite o valor da 1° reta: '))
r2 = float(input('Digite o valor da 2° reta: '))
r3 = float(input('Digite o valor da 3° reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima podem formar triângulos...')
else:
    print('Esses valores não formam um triângulo')
