import requests
from bs4 import BeautifulSoup as soup
import csv

urlb = 'http://store.steampowered.com/search/?specials='

nomesf = []
precob = []
precof = []
desconto = []
preco_sem = []

for i in range(1,46):
    print(i)
    url = urlb + str(i)
    r = requests.get(url)
    p = soup(r.content,'html.parser')

    nomes = p.findAll('span',{'class':'title'})

    for nome in nomes:
        nomesf.append(nome.text)

    precos = p.findAll('div', {'class': 'col search_price discounted responsive_secondrow'})

    for preco in precos:
        preco_sem.append(preco.strike.text.replace('R$ ','').replace(',','.'))
        precob.append(preco.text.replace('\nR$ ','').replace(',','.').replace('R$ ','').replace('\t\t\t\t\t\t\t',''))

for i,preco in enumerate(precob):
    precof.append(preco.replace(preco_sem[i],''))

preco_sem_desconto = [float(i) for i in preco_sem]
preco_final = [float(i) for i in precof]

with open('steam-final.csv', 'a', newline='', encoding='utf8') as f:
    w = csv.writer(f, delimiter=',')
    for i in range(len(nomesf)):
        w.writerow([nomesf[i], preco_sem_desconto[i], preco_final[i]])
