import requests
from bs4 import BeautifulSoup as soup
import csv

urlBase = 'http://steamcharts.com/top/p.'

games = []
jogadoresMax = []
hoursTotal = []
for i in range(1,748):
    if i % 10 == 0:
        print(i)
        
    r = requests.get(urlBase + str(i))
    p = soup(r.content,'html.parser')

    nomes = p.findAll('td',{'class':'game-name left'})
    for nome in nomes:
        games.append(nome.a.text.replace('\n\t\t\t\t\t\t','').replace('\n\t\t\t\t\t',''))

    jogadores_Max = p.findAll('td',{'class':'num period-col peak-concurrent'}) 
    for jogs in jogadores_Max:
        jogadoresMax.append(int(jogs.text))

    hours_total = p.findAll('td',{'class':'num period-col player-hours'})
    for h in hours_total:
        hoursTotal.append(int(h.text))

with open('demanda.csv','w',encoding='utf8') as f:
    w = csv.writer(f, delimiter=',')
    for i in range(len(games)):
        w.writerow([games[i],jogadoresMax[i],hoursTotal[i]])

