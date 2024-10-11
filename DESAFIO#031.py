num1 = float(input('Quantos KM é a viagem: '))
if num1 <=200.0:
    print('Sua viagem não ultrapassou o limite de 200Km, então cada Km custará R$0,50\nValor total da passagem é: ',0.50 * num1)
else:
    print('Sua viagem ultrapassou o limite de 200Km, você pagará a cada Km R$0.45\nValor total da passagem é: ',0.45 * num1)