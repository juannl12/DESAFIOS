n1 = str(input('Uma Frase: ')).upper().strip()
n2 = n1.count('a')
print(f'A letra "a" Apareceu {n2} vezes')
p1 = n1.find('a')
print(f'A primeira letra "A" está posicionada no espaço {p1}')
print('O ultimo "a" da frase está posicionado no espaço',n1.rfind('a'))