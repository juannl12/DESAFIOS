from time import sleep
print('-='*20)
print('         Progessão Aritmética')
print('-='*20)
n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Razão: '))
n3 = int(input('Digite quantas variaveis vc deseja: '))
decimo = n1 + (n3-1) * n2
for c in range(n1, decimo + n2, n2 ):
    sleep(0.2)
    print(f'{c}',end=' ')