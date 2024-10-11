from datetime import date
ano = date.today().year
n1 = int(input('Digite o ano do seu nascimento: '))
n2 = ano - n1
print(f'Quem nasceu em {n1} tem {n2} de idade em {ano}')
if n2 == 18:
    print(f'Você deve se apresentar ao Exército Brasileiro')
elif n2 < 18:
    saldo = 18 - n2
    print(f'Ainda falta {saldo} anos para o alistamento ')
elif n2 > 18:
    saldo = n2 - 18
    print(f'Você já deveria ter se alistado há {saldo} anos')