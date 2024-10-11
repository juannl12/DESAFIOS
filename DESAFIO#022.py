nome= str(input('Digite seu nome Completo: '))
print('Todo em maiúsculo: ',nome.upper())
print('')
print('Todo em minúsculo: ',nome.lower())
print('')
a2 = nome.split()
a3 = len(nome)
a4 = ''.join(a2)
print('Seu nome completo tem',len(a4),'letras sem considerar espaços')
print('')
print('Seu primeiro nome é ',a2[0],'e tem ',len(a2),'letras')



#Juan dos Anjos Lemos