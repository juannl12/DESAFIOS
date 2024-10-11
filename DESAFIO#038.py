n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'O primeiro número "{n1}" é o maior')
elif n2 > n1:
    print(f'O segundo número "{n2} é o maior')
elif n1 == n2:
    print(f'Os 2 valores são iguais "{n1}" e "{n2}"')
