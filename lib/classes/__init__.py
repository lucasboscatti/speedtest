from time import time, sleep
from lib.interface import *
from lib.arquivo import *


class SpeedTest:
    def __init__(self, nome):
        self.nome = nome
        self.tempo = 0

    def joga(self):
        print('A palavra é ...')
        sleep(2)
        palavra = lerArquivo()
        print(f'{cor(1)}{palavra}')
        start = time()
        resposta = str(input(f'{cor(3)}Sua resposta:{cor(0)} ')).title()
        end = time()
        if resposta == palavra:
            t = end - start
            print(f'{cor(4)}{self.nome}{cor(0)} demorou {t:.2f} segundos.')
        else:
            print(f'{cor(1)}Resposta errada! Multa de 10 segundos.{cor(0)}')
            t = 10
        self.tempo += t
        sleep(2)


