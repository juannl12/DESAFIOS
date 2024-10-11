import random
num1 = str(input('1 aluno: '))
num2 = str(input('2 aluno: '))
num3 = str(input('3 aluno: '))
num4 = str(input('4 aluno: '))
lista = [num1, num2, num3,num4]
escolhido = random.choices(lista)
print(f'O sorteado da vez é o {escolhido}')