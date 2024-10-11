n1 = float(input('Digite seu Salário: '))
if n1 <= 1.314:
    novo = n1 + (n1 * 15 / 100)
else:
    novo = n1 + (n1 * 10 / 100)
print(f'Quem ganhava o salário de {n1:.2f} passa a ganhar {novo}')