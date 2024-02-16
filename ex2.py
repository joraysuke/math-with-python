def math(n):
    t_sum = 0
    for i in range(n):
        term = (-1) ** i / (2 * i + 1)
        t_sum += term
    return t_sum * 4

terms = int(input('Insira a quantidade de termos: '))
pi= math(terms)

print(f'π = {pi}')
