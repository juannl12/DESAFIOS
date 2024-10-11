print('=============== Digite uma sequencia de números ===============\n')
a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificar o maior...
if a > b and a > c:
    maior = a
if b > a and b > c :
    maior = b
if c > a and c > b:
    maior = c
print(f'O MAIOR valor digitado foi {menor}')
print(f'O MENOR valor digitado foi {maior}')
