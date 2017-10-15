import requests
from bs4 import BeautifulSoup as soup
import csv

urlb = 'http://store.steampowered.com/search/?page='

nomesf = [] 
precob = [] 
precof = [] 
desconto = [] 
preco_sem = [] 

for i in range(1,1434): # número de páginas
    print(i) # para controle do número da página, em caso de erros
    url = urlb + str(i) 
    r = requests.get(url)
    p = soup(r.content,'html.parser')

    nomes = p.findAll('span',{'class':'title'}) # conteiner do elemento que contém o nome

    for nome in nomes:
        nomesf.append(nome.text) 

    precos = p.findAll('div', {'class': 'col search_price discounted responsive_secondrow'}) # conteiner do elemeno que contem os precos
    
    for preco in precos:
        preco_sem.append(preco.strike.text.replace('R$ ','').replace(',','.')) # preco sem desconto
        precob.append(preco.text.replace('\nR$ ','').replace(',','.').replace('R$ ','').replace('\t\t\t\t\t\t\t','')) # preco com desconto

for i,preco in enumerate(precob):
    precof.append(preco.replace(preco_sem[i],'')) 

preco_sem_desconto = [float(i) for i in preco_sem]
preco_final = [float(i) for i in precof]

with open('steam-final.csv', 'a', newline='', encoding='utf8') as f:
    w = csv.writer(f, delimiter=',')
    for i in range(len(nomesf)):
        w.writerow([nomesf[i], preco_sem_desconto[i], preco_final[i]])
