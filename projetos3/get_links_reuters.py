import requests
from bs4 import BeautifulSoup as soup

links = []
base = 'https://www.reuters.com'
for i in range(0,599):
    print(i)
    url = 'https://www.reuters.com/news/archive/brazil-news?view=page&page={}&pageSize=10'.format(i) # ateh 599

    r = requests.get(url)
    p = soup(r.content,'html.parser')

    c = p.findAll('div',{'class':'story-content'})
    for k in c:
        links.append(base + k.a['href'])

with open('reuters.txt','a') as f:
    f.write('\n'.join(links))