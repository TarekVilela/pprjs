import requests
from bs4 import BeautifulSoup as soup
import csv
import time

def baixar(arquivo, tipo):

    for casca in range(34):

        while True:
            try:

                if tipo == 'filmes':
                    url = 'https://thepiratebay.org/browse/200/%s/7' % (casca)
                elif tipo == 'jogos':
                    url = 'https://thepiratebay.org/browse/401/%s/7' % (casca)
                else:
                    print('filmes ou jogos')

                link = requests.get(url)
                link.raise_for_status()

                page = soup(link.content, 'html.parser')

                c_nomes = page.findAll('div', {'class': 'detName'})

                c_seeders = page.findAll('td', {'align': 'right'})

                nomes = []
                for i in c_nomes:
                    nomes.append(i.a.text.replace('|',''))

                sl = []
                for i in c_seeders:
                    sl.append(i.text)

                seeders = []
                for i in sl[0:len(sl):2]:
                    seeders.append(i)

                leechers = []
                for i in sl[1:len(sl):2]:
                    leechers.append(i)


                with open(arquivo, 'a', newline='',encoding='utf8') as f:
                    w = csv.writer(f, delimiter=',')
                    for i in range(len(nomes)):

                        w.writerow([nomes[i], seeders[i], leechers[i]])

                print(casca)

            except:
                print('erro', casca)
                continue

            break


print('Insira o número do dia:')
numero = input('> ')
start = time.time()
arquivo_filmes = 'dados-'+numero+'-filmes.csv'
arquivo_jogos = 'dados-'+numero+'-jogos.csv'

baixar(arquivo_filmes, 'filmes')
baixar(arquivo_jogos,'jogos')
print(time.time()-start)