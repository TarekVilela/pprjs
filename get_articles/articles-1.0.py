import requests
from bs4 import BeautifulSoup as soup

def entrar(par):
    r = requests.get(par)
    p = soup(r.content,'html.parser')
    return p

def escrever(titulo,article,jornal,manch=None):

    if manch != None:
        with open(titulo + '['+jornal+'].txt','w') as f:
            f.write(titulo + '\n' + manch + '\n\n\n\t')
            f.write('\n\n\t'.join(map(str, article)))
    else:
        with open(titulo + '['+jornal+'].txt','w') as f:
            f.write(titulo + '\n\n\n\t')
            f.write('\n\n\t'.join(map(str, article)))

def transformar(paragraphs):

    article = []
    for paragraph in paragraphs:
        article.append(paragraph.text)
    return article

def is_singular(par):

    if par[-4:] != '.txt':
        sing = True
    else:
        sing = False
    return sing

def Atlantic(par):

    p = entrar(par)
    titulo = p.findAll('div', {'class': 'article-cover-content'})[0].h1.text
    manch = p.findAll('div', {'class': 'article-cover-content'})[0].p.text
    paragraphs = p.findAll('div', {'class': 'article-body'})[0].findAll('p')
    article = transformar(paragraphs)
    escrever(titulo,article,'Atlantic',manch)

def Yahoo(par):

    p = entrar(par)
    titulo = p.findAll('h1',{'itemprop':'headline'})[0].text
    paragraphs = p.findAll('article',{'itemprop':'articleBody'})[0].findAll('p')
    article = transformar(paragraphs)
    escrever(titulo, article, 'Yahoo')

def G1(par):

    p = entrar(par)
    titulo = p.findAll('h1',{'itemprop':'headline'})[0].text
    manch = p.findAll('h2',{'itemprop':'alternativeHeadline'})[0].text
    paragraphs = p.findAll('article',{'itemprop':'articleBody'})[0].findAll('p')
    article = transformar(paragraphs)
    escrever(titulo, article, 'G1', manch)

def Estadao(par):

    p = entrar(par)
    titulo = p.findAll('article')[0].h1.text
    manch = p.findAll('article')[0].h2.text
    paragraphs = p.findAll('div',{'class':'box area-select'})[0].findAll('p')
    article = transformar(paragraphs)
    escrever(titulo, article, 'Estadão', manch)

def nyt(par):

    p = entrar(par)
    titulo = p.findAll('h1',{'itemprop':'headline'})[0].text
    paragraphs = p.findAll('main',{'class':'main'})[0].findAll('p')
    article = []
    article = transformar(paragraphs)
    escrever(titulo, article, 'NYT')

def fox(par):

    p = entrar(par)
    titulo = p.findAll('h1',{'class':'headline head1'})[0].text
    paragraphs = p.findAll('div',{'class':'article-body'})[0].findAll('p')
    bios = p.findAll('div',{'class':'author-bio'})
    article = transformar(paragraphs)
    escrever(titulo, article, 'Fox News')

def guardian(par):

    p = entrar(par)
    titulo = p.findAll('h1',{'class':'content__headline'})[0].text
    manch = p.findAll('meta',{'itemprop':'description'})[0]['content']
    paragraphs = p.findAll('div',{'class':'content__article-body from-content-api js-article__body'})[0].findAll('p')
    article = transformar(paragraphs)
    escrever(titulo, article, 'Guardian', manch)

def BBC(par):

    p = entrar(par)
    titulo = p.findAll('div',{'class':'story-body'})[0].h1.text
    paragraphs = p.findAll('div',{'class':'story-body'})[0].findAll('p')
    article = transformar(paragraphs)
    escrever(titulo, article, 'BBC')

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
        elif 'nytimes' in link:
            nyt(link)
        elif 'foxnews' in link:
            fox(link)
        elif 'guardian' in link:
            guardian(link)
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

get_article('ar.txt')