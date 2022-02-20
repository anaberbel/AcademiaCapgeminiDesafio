def auxilia_senha():
    while True:
        senha = input('Insira a sua sennha: ')
        tamanho_minimo = 6
        diferenca_de_tamanho = tamanho_minimo - len(senha)
        caracteres_especiais = '!@#$%^&*()-+'
        dicionario = {
            "maiscula": True,
            "minuscula": True,
            "especial": True,
            "digito": True,
        }

        for caractere in senha:
            if caractere.isdigit() and dicionario["digito"]:
                dicionario["digito"] = False
            elif caractere.isupper() and dicionario["maiscula"]:
                dicionario["maiscula"] = False
            elif caractere.islower() and dicionario["minuscula"]:
                dicionario["minuscula"] = False
            else:
                for i in caracteres_especiais:
                    if caractere == i and dicionario["especial"]:
                        dicionario["especial"] = False
                        break

        num = sum(dicionario.values())

        if diferenca_de_tamanho > 0:
            if diferenca_de_tamanho >= num:
                print(diferenca_de_tamanho)
            else:
                print(num)
        else:
            if num > 0:
                print(num)
            else:
                break

auxilia_senha()
