import random
n1 = int(input('Digite um numero de 1 a 10 q o computador está \npensando em seus componentes: '))
n2 = random.randint(1,10)
print(f'o numero escolhido é: {n2}')
if n1 == n2:
    print('Você acertou o número, Parabéns!!!')
else: print('Você errou o número.\n\nTente novamente...')