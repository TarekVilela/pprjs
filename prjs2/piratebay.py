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
                sl = []
                seeders = []
                leechers = []
                
                for a,b,c,d in zip(c_nomes,c_seeders,s1[0:len(s1):2],s1[1:len(s1):2]):
                    nomes.append(a.a.text.replace('|',''))
                    sl.append(b.text)
                    seeders.append(c)
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
