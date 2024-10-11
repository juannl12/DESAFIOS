from datetime import date
ano = date.today().year
n2 = int(input('Data de Nascimento: '))
#Cálculo de ano de nascimento = n3
n3 = ano - n2
if n3 <= 9:
    print('Mirim')
elif n3 >= 10 and n3 <= 14:
    print('Infantil')
elif n3 >= 15 and n3 <= 19:
    print('Junior')
elif n3 == 20:
    print('Sênior')
elif n3 > 20:
    print('Master')