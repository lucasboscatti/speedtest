from lib.interface import *
from lib.funcoes import *


def main():
    while True:
        resposta = menu('MENU PRINCIPAL', ['Jogar', 'Mudar as configurações', 'Sair'])
        if resposta == 3:
            cabecalho(f'{"Saindo do sistema... Até logo!":^42}')
            break
        elif resposta == 2: 
            configuracoes()
        elif resposta == 1:
            jogar()
        else:
            print(f'{cor(1)}ERRO! Digite uma opção válida!{cor(0)}')


main()
