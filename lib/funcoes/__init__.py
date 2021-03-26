from lib.interface import *
from lib.classes import SpeedTest
from operator import attrgetter
from time import sleep


def configuracoes(jogadores=2, rodadas=5):
    while True:
        resposta = menu('CONFIGURAÇÕES', ['Alterar o número de jogadores', 'Alterar o número de rodadas'])
        if resposta not in [1, 2]:
            print(f'{cor(1)}ERRO! Digite uma opção válida!{cor(0)}')
        else:
            if resposta == 1:
                jogadores = alteracao(f'{cor(3)}Número de jogadores {cor(1)}( 2 a 4 ): ', 2)
            elif resposta == 2:
                rodadas = alteracao(f'{cor(3)}Número de rodadas {cor(1)}( 2 a 10 ): ', 1)
            continuar = str(input(f'{cor(3)}Continuar alterações? {cor(1)}( S / N ){cor(0)}')).upper()
            if continuar == 'N':
                jogar(jogadores, rodadas)
                break
            elif continuar == 'S':
                pass
            else:
                print(f'{cor(1)}ERRO! Digite apenas S ou N!{cor(0)}')


def jogar(jogadores=2, rodadas=5):
    lista_jogadores = nomeJogadores(jogadores)
    cabecalho('VAMOS JOGAR!')
    num_rodadas = 0
    while num_rodadas < rodadas:
        cabecalho(f'{num_rodadas + 1}ª RODADA')
        for i in range(0, len(lista_jogadores)):
            print(f'Quem joga agora é: {cor(4)}{lista_jogadores[i].nome}{cor(0)}')
            lista_jogadores[i].joga()
            print(linha())
        num_rodadas += 1
    ranking(lista_jogadores)


def ranking(lista_jogadores):
    jogadores = sorted(lista_jogadores, key=attrgetter('tempo'))
    print(f'O vencedor é: {cor(4)}{jogadores[0].nome}{cor(0)}!\nCom um tempo de {cor(4)}{jogadores[0].tempo:.2f}{cor(0)} segundos.')
    print(f'{cor(1)}Parabéns,{cor(4)} {jogadores[0].nome}!{cor(0)}')
    cabecalho('RANKING')
    print('Position            Player            Time')
    print()
    for i in range(0, len(jogadores)):
        print(f'{i + 1:>4}°   {jogadores[i].nome:>18}     {jogadores[i].tempo:>11.2f}')


def alteracao(txt, config, min=2, max_rodadas=10, max_jogador=4):
    while True:
        quantidade = leiaInt(txt)
        if config == 1:
            if quantidade < min or quantidade > max_rodadas:
                print(f'{cor(1)}ERRO! Digite um valor válido!{cor(0)}')
            else:
                return quantidade
        elif config == 2:
            if quantidade < min or quantidade > max_jogador:
                print(f'{cor(1)}ERRO! Digite um valor válido!{cor(0)}')
            else:
                return quantidade


def nomeJogadores(jogadores):
    jogador1 = SpeedTest(str(input(f'{cor(3)}Nome {cor(4)}jogador 1:{cor(0)} ')).title())
    jogador2 = SpeedTest(str(input(f'{cor(3)}Nome {cor(4)}jogador 2:{cor(0)} ')).title())
    lista = [jogador1, jogador2]
    if jogadores >= 3:
        jogador3 = SpeedTest(str(input(f'{cor(3)}Nome {cor(4)}jogador 3:{cor(0)} ')).title())
        lista.append(jogador3)
        if jogadores == 4:
            jogador4 = SpeedTest(str(input(f'{cor(3)}Nome {cor(4)}jogador 4:{cor(0)} ')).title())
            lista.append(jogador4)
    return lista
