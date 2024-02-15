numero = float(input('Escreva um número: '))

if 0 <= numero <= 2:
    print('o valor correspondente é X')
elif 2 <= numero <= 3.5:
    print('o valor correspondente é 2')
elif 3.5 <= numero <= 5:
    print('o valor correspondente é 3')
elif numero > 5:
    conta = ((numero**2) - (10*numero)+28)
    print(f'o valor correspondente é {conta} ')
else:
    print('número inválido!')

