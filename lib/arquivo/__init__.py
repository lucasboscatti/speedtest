from bs4 import BeautifulSoup
import requests
from random import choice


def webScrapPalavras():
    with open('palavras_file.txt', 'w', encoding='iso-8859-1') as palavras_file:
        for i in range(0, 200):
            url = 'https://www.palavrasque.com/palavra-aleatoria.php?Submit=Nova+palavra'
            html_text = requests.get(url).text
            soup = BeautifulSoup(html_text, 'lxml')
            palavra = soup.find_all('b')
            if len(palavra[0].text) > 6:
                palavras_file.write(f'{palavra[0].text}\n')
                print(palavra[0].text)
        palavras_file.close()
        print('fim')


def lerArquivo():
    with open('lib/arquivo/palavras_file.txt', 'r', encoding='utf-8') as palavras_file:
        palavras = palavras_file.read().splitlines()
        return choice(palavras)