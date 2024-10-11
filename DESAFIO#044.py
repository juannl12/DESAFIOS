n1 = int(input('Qual é o preço do produto: '))
print('\n1. À vista dinheiro/cheque: 10% de desconto')
print('2. À vista no cartão: 5% de desconto')
print('3. Em até 2x no cartão: Preço normal')
print('4. 3x ou mais no cartão: 20% de juros')
n2 = int(input('\nForma de pagamento: '))
#Cálculo do desconto (10%) = n3
n3 = (n1*10)/100
t1 = n1 - n3
#Cálculo do desconto (5%) = n4
n4 = (n1*5)/100
t2 = n1 - n4
#Cálculo do juros (20%) = n5
n5 = (n1*20)/100
if n2 == 1:
    print('Você escolheu a opção "À vista dinheiro/cheque: 10% de desconto"')
    print(f'O preço do produto ficará em {t1}')
elif n2 == 2:
    print('Você escolheu a opção "À vista no cartão: 5% de desconto"')
    print(f'O preço do produto ficará custando R${t2}')
elif n2 == 3:
    print('Você escolheu a opção "Em até 2x no cartão: Preço normal"')
    print(f'O preço do produto ficará custando R${n1}')
elif n2 == 4:
    print('Você escolheu a opção "3x ou mais no cartão: 20% de juros"')
    print(f'Cada parcela do produto ficará custando R${n5}')
else:
    print('Ocorreu um erro\nProvavelmente você selecionou alguma opção errada\n\nTente novamente...')