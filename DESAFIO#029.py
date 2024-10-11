print('\n\nVocê passou em um radar de 80KM/h\n\n')
n1 = float(input('qual a velocidade q vc passou no radar de 80Km/h: '))
n2 = (n1-80) * 7
if n1 >=80.0:
    print(f'Você foi multado em R${n2:.2f}')
else:
    print('Você não foi multado')