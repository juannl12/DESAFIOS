print('Digite suas notas de uma matéria a cada bimestre e descubra sua média do ano em 4 Bimestres')
n1 = float(input('Nota 1B : '))
n2 = float(input('Nota 2B: '))
n3 = float(input('Nota 3B: '))
n4 = float(input('Nota 4B: '))
t = (n1+n2+n3+n4)/4
print('Sua média do ano é: "{:^3}"'.format(t))
input('Aperte ENTER para sair')