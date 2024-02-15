a = float(input('Adicione um valor para ''a'': '))
b = float(input('Adicione um valor para ''b'': '))
c = float(input('Adicione um valor para ''c'': '))

def equacao(a,b,c):
    conta = (b**2 - 4*a*c)
    delta = conta **0.5


    if conta >= 0 and a != 0 and b !=0 and c!= 0:
        x1 = (-b + delta)/(2*a)
        x2 = (-b - delta)/(2*a)
        print(f'O valor de x1 é {x1} e o valor de x2 é {x2}.')
    else:
        print('Raiz inválida.')


equacao(a,b,c)

