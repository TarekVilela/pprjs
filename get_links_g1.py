import requests
from bs4 import BeautifulSoup as soup

links = []

for i in range(0,2000):
    print(i)
    url = 'http://g1.globo.com/economia/index/feed/pagina-{}.html'.format(i)

    r = requests.get(url)
    p = soup(r.content,'html.parser')

    c = p.findAll('div',{'class':'feed-post-body-title gui-color-primary gui-color-hover '})

    for k in c:
        links.append(k.a['href'])

with open('links.txt','a') as f:
    f.write('\n'.join(links))