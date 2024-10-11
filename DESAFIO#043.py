print('-='*25)
print('                Calculo de IMC            ')
print('-='*25)
peso = float(input('Digite seu peso em KG: '))
n2 = float(input('Digite sua altura em cm: '))
#Cálculo altura para metros = "altura"
altura = (n2/100)**2
#Cálculo IMC = n4
n4 = peso/altura
print('\nQuando o resultado do IMC está entre \n18,5 e 24,9, a pessoa tem peso normal.')
print(f'\nSeu IMC é {n4:.1f}')
if n4 <= 18.5:
    print('Você está abaixo do peso')
elif n4 >= 18.5 and n4 <= 25:
    print('Você está com o peso Ideal')
elif n4 >= 25 and n4 <= 30:
    print('Você está com sobrepeso')
elif n4 >= 30 and n4 <= 40:
    print('Você está com obesidade')
elif n4 >= 40:
    print('Você está com obesidade mórbida')
else:
    print('Não foi possível calcular o IMC.\nTente novamente...')