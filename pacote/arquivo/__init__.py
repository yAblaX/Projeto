from pacote.cores import *
from time import sleep


# CONFIRMA SE O ARQUIVO EXISTE #
def arquivo_existe(arquivo):
    try:
        a = open(arquivo, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# CRIA UM ARQUIVO #
def criar_arquivo(x):
    y = open(x, 'w')
    y.close()
    print(verde('Arquivo criado com sucesso'))
    sleep(1)


# CADASTRAR PESSOAS #
def cadastro(arquivo, nome, peso, altura, idade):
    arq = open(arquivo, 'a')
    arq.write(str(f'{nome} {peso} {altura} {idade} \n'))
    arq.close()


# MOSTRA AS PESSOAS CADASTRADAS #
def ver_cadastradas(arquivo):
    arq = open(arquivo, 'rt')
    print(f'|{"Nome":^14}|{"Peso":^14}|{"Altura":^14}|{"Idade":^13}|')
    for linha in arq:
        dado = linha.split(' ')
        if type(dado[1]) != int and type(dado[1]) != float:
            print(f'|{dado[0]:^14}|{f"{dado[1]}Kg":^14}|{dado[2]:^14}|{dado[3]:^13}|')
