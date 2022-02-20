def construir(numero):
    cont = 1
    while cont <= numero:
        print(' ' * (numero - cont) + '*' * cont)
        cont += 1


quantidade = int(input())
construir(quantidade)
