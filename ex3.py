def pi(n):
    soma = 0
    for i in range(1,n+1):
        termo = (-1)**(i-1)*4/(2*i-1)
        soma += termo
        print (soma)
    return soma

n = int(input('Digite a quantidade de termos que você quer somar para achar PI: '))
pi(n)
