from random import shuffle,randint
print('--------------- Sorteador de times --------------- \n')

n1 = str(input('  1 Player: ')).strip().capitalize()
n2 = str(input('  2 Player: ')).strip().capitalize()
n3 = str(input('  3 Player: ')).strip().capitalize()
n4 = str(input('  4 Player: ')).strip().capitalize()
n5 = str(input('  5 Player: ')).strip().capitalize()
n6 = str(input('  6 Player: ')).strip().capitalize()
n7 = str(input('  7 Player: ')).strip().capitalize()
n8 = str(input('  8 Player: ')).strip().capitalize()
n9 = str(input('  9 Player: ')).strip().capitalize()
n10 = str(input('  10 Player: ')).strip().capitalize()
lista = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
shuffle(lista)
print('\n  Os primeiros 5 nomes é o time da DEFESA\n ',lista,'\n\n\n\n')
#
#
print('=============== Sorteador de Mapas ===============\n')
print('Fracture, Breeze, Abyss, Split e Pearl não estão no sorteador\n')
input('                  Aperte ENTER para sortear o mapa\n')
#
#
a1 = print('  1- Ascent')
a2 = print('  2- Bind')
a3 = print('  3- Icebox')
a4 = print('  4- Haven')
a5 = print('  5- Lotus')
a6 = print('  6- Sunset')
maps = [a1,a2,a3,a4,a5,a6]
t = randint(1,6,)
print(f'\n                  Mapa {t} foi escolhido\n\n\n\n\n\n\n')

input('Aperte ENTER para sair =)... ')
#
#                                  *codigo feito no dia 14/08/2024
#   *atualizado em xx/xx/xxxx