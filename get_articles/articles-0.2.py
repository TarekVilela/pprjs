import requests
from bs4 import BeautifulSoup as soup

def is_singular(par):

    if par[-4:] != '.txt':
        sing = True
    else:
        sing = False

    return sing

def Atlantic(par):

    r = requests.get(par)
    p = soup(r.content, 'html.parser')

    titulo = p.findAll('div', {'class': 'article-cover-content'})[0].h1.text
    manch = p.findAll('div', {'class': 'article-cover-content'})[0].p.text

    paragraphs = p.findAll('div', {'class': 'article-body'})[0].findAll('p')

    article = []
    for paragraph in paragraphs:
        article.append(paragraph.text)

    with open(titulo + '[Atlantic]' +'.txt', 'w') as f:
        f.write(titulo + '\n' + manch + '\n\n\n\t')
        f.write('\n\n\t'.join(map(str, article)))


def Yahoo(par):

    r = requests.get(par)
    p = soup(r.content,'html.parser')

    titulo = p.findAll('h1',{'itemprop':'headline'})[0].text

    paragraphs = p.findAll('article',{'itemprop':'articleBody'})[0].findAll('p')

    article = []
    for paragraph in paragraphs:
        article.append(paragraph.text)

    with open(titulo + '[Yahoo]' +  '.txt', 'w') as f:
        f.write(titulo + '\n\n\n\t')
        f.write('\n\n\t'.join(map(str, article)))

def G1(par):

    r = requests.get(par)
    p = soup(r.content,'html.parser')

    titulo = p.findAll('h1',{'itemprop':'headline'})[0].text
    manch = p.findAll('h2',{'itemprop':'alternativeHeadline'})[0].text

    paragraphs = p.findAll('article',{'itemprop':'articleBody'})[0].findAll('p')

    article = []
    for paragraph in paragraphs:
        article.append(paragraph.text)

    with open(titulo + '[Yahoo]' + '.txt', 'w') as f:
        f.write(titulo + '\n' + manch + '\n\n\n\t')
        f.write('\n\n\t'.join(map(str, article)))

def Estadao(par):

    r = requests.get(par)
    p = soup(r.content,'html.parser')


    titulo = p.findAll('article')[0].h1.text
    manch = p.findAll('article')[0].h2.text

    paragraphs = p.findAll('div',{'class':'box area-select'})[0].findAll('p')

    article = []
    for paragraph in paragraphs:
        article.append(paragraph.text)

    with open(titulo + '[Yahoo]' + '.txt', 'w') as f:
        f.write(titulo + '\n' + manch)
        f.write('\n\n\t'.join(map(str, article)))

def get_article(par):

    def baixar(link):
        if 'atlantic.com' in link:
            Atlantic(link)
        elif 'yahoo.com' in link:
            Yahoo(link)
        elif 'g1' in link:
            G1(link)
        elif 'estadao' in link:
            Estadao(link)
        else:
            print('site não suportado')

    if is_singular(par) == True:
        baixar(par)

    elif is_singular(par) == False:
        with open(par) as f:
            lista = f.readlines()
            lista = [x.strip() for x in lista]

            for i, item in enumerate(lista):
                print('Baixando (%i/%i): ' % (i+1,len(lista)),item)
                baixar(item)
