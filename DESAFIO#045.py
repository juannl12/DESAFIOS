import random
from time import sleep
print('=-'*9)
print('     Jokenpo')
print('=-'*9)
print('\n[ 0 ] = Pedra')
print('[ 1 ] = Papel')
print('[ 2 ] = Tesoura\n')
player = int(input('Digite um valor: '))
print('JO')
sleep(0.5)
print('Ken')
sleep(0.5)
print('PO!!!')
pc = random.randint(0,2)
if pc == 0: # pedra
    if player == 0: #EMPATE
        print('Joguei Pedra')
        print(f'Você jogou {player}')
        sleep(1)
        print('Empatou.\nVamos de novo')
    elif player == 1: #pedra + papel == papel
        print('Joguei Papel')
        print(f'Você jogou {player}')
        sleep(1)
        print('Perdi')
    elif player == 2: #pedra + tesoura == pedra
        print('Joguei Tesoura')
        print(f'Você jogou {player}')
        sleep(1)
        print('Ganhei!!!')
    else:
        print('JOGADA INVÁLIDA')
#
elif pc == 1:  # papel
    if player == 0: #papel + pedra == papel
        print('Joguei Pedra')
        print(f'Você jogou {player}')
        sleep(1)
        print('Ganhei!!!')
    elif player == 1: #EMPATE
        print('Joguei Papel')
        print(f'Você jogou {player}')
        sleep(1)
        print('Empatou.\nVamos de novo')
    elif player == 2: #papel + tesoura == tesoura
        print('Joguei Tesoura')
        print(f'Você jogou {player}')
        sleep(1)
        print('Perdi')
    else:
        print('JOGADA INVÁLIDA')
#
elif pc == 2: #tesoura
    if player == 0: #tesoura + pedra == pedra
        print('Joguei Pedra')
        print(f'Você jogou {player}')
        sleep(1)
        print('perdi!!!')
    elif player == 1: #tesoura + papel == tesoura
        print('Joguei Papel')
        print(f'Você jogou {player}')
        sleep(1)
        print('Perdi')
    elif player == 2: #EMPATE
        print('Joguei Tesoura')
        print(f'Você jogou {player}')
        sleep(1)
        print('Empatou.\nVamos de novo')
    else:
        print('JOGADA INVÁLIDA')
sleep(2)
input('\nAperte enter para sair...')