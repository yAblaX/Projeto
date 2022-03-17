from pacote.cores import *


def linha():
    print('=' * 60)


def menu(txt):
    linha()
    print(f'{f"{txt}":^60}')
    linha()


def escolhas(lista):
    for c in range(3):
        print(f'{c + 1} - {lista[c]}')