import requests
from bs4 import BeautifulSoup as soup
import csv
import time

articles = []
dates = []

with open('links_reuters.txt') as f:
    for line in f:

        try:
            print(line.rstrip())
            r = requests.get(line.rstrip())
            p = soup(r.text,'html.parser')
        
            title = p.findAll('h1',{'class':'ArticleHeader_headline'})[0].text
            date = p.findAll('div',{'class':'ArticleHeader_date'})[0].text.split(' / ')[0]

            paragraphs = p.findAll('div',{'class':'StandardArticleBody_body'})[0].findAll('p')

            article = []
            article.append(title)
            for p in paragraphs:
                article.append(p.text)

            articles.append(article)
            dates.append(date)

        except:
            pass

dates2 = []
for i in dates:
    t = time.strptime(i,'%B %d, %Y')
    dates2.append(time.strftime('%Y-%m-%d',t))

with open('teste.csv', 'a', newline='', encoding='utf8') as f:
    w = csv.writer(f, delimiter=',')
    for i in range(len(articles)):
        w.writerow([dates2[i], articles[i]])