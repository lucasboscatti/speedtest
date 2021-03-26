def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def cor(nome):
    cores = {'0': '\033[m',  # 0 - sem cores
             '1': '\033[1;31m',  # 1 - vermelho
             '2': '\033[1;32m',  # 2 - verde
             '3': '\033[1;33m',  # 3 - amarelo
             '4': '\033[1;34m',  # 4 - azul
             '5': '\033[1;35m',  # 5 - roxo
             '6': '\033[7;30m'  # 6 - branco
             }
    return cores[f'{nome}']


def menu(titulo, lista):
    cabecalho(titulo)
    for i, k in enumerate(lista):
        print(f'{cor(3)}{i + 1}{cor(0)} - {cor(4)}{k}{cor(0)}')
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc


def leiaInt(txt):
    while True:
        try:
            n = int(input(f'{cor(3)}{txt}{cor(0)}'))
        except (ValueError, TypeError):
            print(f'{cor(1)}ERRO! Por favor digite um número inteiro válido.{cor(0)}')
            continue
        except KeyboardInterrupt:
            print(f'{cor(1)}O usuário prefiriu parar o programa.{cor(0)}')
            return 0
        else:
            return n


