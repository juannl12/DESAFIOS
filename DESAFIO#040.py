print('========================= Média Escolar =========================')
n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua nota: '))
#Cálculo da média = n3
n3 = (n1 + n2)/2
if n3 <= 4.9:
    print(f'Você está reprovado,pos sua média é "{n3}"')
elif n3 >= 5.0 and n3 <= 6.9:
    print(f'Você está de recuperação,pos sua média é "{n3}"')
elif n3 > 6.9:
    print(f'Você foi aprovado,pos sua média é "{n3}"')