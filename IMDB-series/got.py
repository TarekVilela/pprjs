import requests
from bs4 import BeautifulSoup as soup
import csv

def pegar_dados_imdb(nome,link,temporadas):
    print(nome)
    r = []
    q = []
    nomes = []
    temps = []

    for i in range(1,temporadas+1):
        print('trabalhando na temporada ',i)
        url1 = link + str(i)
        h1 = requests.get(url1)
        p1 = soup(h1.content,'html.parser')

        c1 = p1.findAll('div',{'itemprop':'episodes'})

        for j in range(len(c1)):
            nomes.append(c1[j].strong.text)

        for k in range(len(c1)):
            url2 = 'http://imdb.com' + c1[k].strong.a['href']
            h2 = requests.get(url2)
            p2 = soup(h2.content,'html.parser')
            c2 = p2.findAll('span',{'itemprop':'ratingValue'})
            c21 = p2.findAll('span',{'itemprop':'ratingCount'})

            for m in range(len(c2)):
                r.append(c2[m].text)
                q.append(c21[m].text)

        for l in range(1,len(c1)+1):
            temps.append('S'+str(i))
    
    q = [int(m.replace('"','').replace(',','')) for m in q]

    with open(nome+'.csv', 'a', newline='', encoding='utf8') as f:
        w = csv.writer(f, delimiter=',')
        for i in range(len(nomes)):
            w.writerow([nomes[i], q2[i], r[i],temps[i]])
