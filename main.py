from pacote.cores import *
from pacote.menu import *
from pacote.arquivo import *
from os import system
from time import sleep

lista = ['Cadastrar nova pessoa', 'Ver cadastrados', 'Sair']
arquivo = 'arquivo.txt'
system('cls')

if arquivo_existe(arquivo):
    print(verde('Arquivo encontrado com sucesso'))
    sleep(1)
else:
    criar_arquivo(arquivo)

system('cls')

while True:
    system('cls')
    menu('MENU')
    escolhas(lista)
    linha()

    try:
        opc = int(input('Digite: '))

        if opc == 1:
            system('cls')
            menu('CADASTRAR PESSOAS')
            nome = str(input('Primeiro nome: '))
            peso = float(input('Peso: '))
            altura = float(input('Altura: '))
            idade = int(input('Idade: '))
            cadastro(arquivo, nome, peso, altura, idade)

        elif opc == 2:
            system('cls')
            menu('PESSOAS CADASTRADAS')
            ver_cadastradas(arquivo)
            linha()
            input('Digite "ENTER" para continuar')

        elif opc == 3:
            break

    except:
        print(vermelho('Resposta inválida, escolha 1, 2 ou 3'))
        sleep(3)
