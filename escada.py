def construir(numero):
    cont = 1
    while cont <= numero:
        print(' ' * (numero - cont) + '*' * cont)
        cont += 1


quantidade = int(input('Informe a quantidade de degraus: '))
construir(quantidade)
