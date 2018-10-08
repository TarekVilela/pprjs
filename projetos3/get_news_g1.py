import requests
from bs4 import BeautifulSoup as soup
import csv

articles = []
dates = []

with open('links_g1.txt') as f:
    for line in f:
        
        try:
            print(line.rstrip())
            r = requests.get(line.rstrip())
            p = soup(r.text,'html.parser')

            title = p.findAll('h1',{'class':'content-head__title'})[0].text
            subtitle = p.findAll('div',{'class':'medium-centered subtitle'})[0].h2.text
            date = p.findAll('p',{'class':'content-publication-data__updated '})[0].time['datetime'][0:10]

            paragraphs = p.findAll('article',{'itemprop':'articleBody'})[0].findAll('p')

            article = []
            article.append(title)
            article.append(subtitle)
            for p in paragraphs:
                article.append(p.text)

            articles.append(article)
            dates.append(date)

        except:
            pass

with open('g1_final.csv', 'a', newline='', encoding='utf8') as f:
    w = csv.writer(f, delimiter=',')
    for i in range(len(articles)):
        w.writerow([dates[i], articles[i]])