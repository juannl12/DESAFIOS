print('=-=-=-=-=-=-=-=- Empréstimo Bancário =-=-=-=-=-=-=-=-\n\n')
n1 = int(input('Qual é o valor do empréstimo: '))
n2 = float(input('Qual é o seu sálario: '))
n3 = int(input('Em quantos anos você vai pagar: '))
#Cálculo dos meses = n4...
n4 = n3 * 12
#Cálculo da prestação...
n5 = n1 / n4
#Cálculo do Salário "30%" = n5...
n6 = n2 * 30 / 100
if n5 > n6:
    print(
        f'EMPRÉSTIMO NEGADO\n\nNós do banco só aceitamos se o cliente possuir 1 parcela em 30% do sálario\n30% do seu sálario é R${n6:.2f}')
elif n5 < n6:
    print(f'ACESSO PERMITIDO\n\nParabéns Você recebeu seu Empréstimo de R${n1}')
print(f'As parcelas ficaram em cada mês ficaram em R${n5:.2f}')