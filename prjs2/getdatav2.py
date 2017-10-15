import requests
from bs4 import BeautifulSoup as soup
import csv

urlb = 'http://store.steampowered.com/search/?page='

nomes = []
preco_original = []
preco_final = []

for i in range(1,3):
    print(i)
    url = urlb + str(i)
    r = requests.get(url)
    p = soup(r.content,'html.parser')

    cont = p.findAll('div',{'class':'responsive_search_name_combined'})

    for i in cont:
        if not i.findAll('div',{'class':'col search_price responsive_secondrow'}):
            nomes.append(i.span.text)
            preco_original_bruto = i.strike.text
            preco_bruto = i.findAll('div',{'class':'col search_price discounted responsive_secondrow'})[0]
            preco_final_limpo = preco_bruto.text.replace('\n'+preco_original_bruto+'R$ ','').replace('\t\t\t\t\t\t\t','').replace(',','.')
            if 'Free' in preco_final_limpo:
                preco_final_limpo = '0'
            preco_original.append(preco_original_bruto.replace('R$ ','').replace(',','.'))
            preco_final.append(preco_final_limpo)

        else:
            nomes.append(i.span.text)
            preco_final_bruto = i.findAll('div',{'class':'col search_price responsive_secondrow'})[0].text
            preco_final_limpo = preco_final_bruto.replace('\r\n\t\t\t\t\t\t\t\tR$ ','').replace('\t\t\t\t\t\t\t','').replace(',','.').replace('\r\n\tFree to Play','0').replace('\n','0')
            preco_original.append(preco_final_limpo)
            preco_final.append(preco_final_limpo)

preco_original = [float(i) for i in preco_original]
preco_final = [float(i) for i in preco_final]

with open('steam-tdos.csv', 'a', newline='', encoding='utf8') as f:
    w = csv.writer(f, delimiter=',')
    for i in range(len(nomes)):
        w.writerow([nomes[i], preco_original[i], preco_final[i]])
