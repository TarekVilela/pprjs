from bs4 import BeautifulSoup as soup
import requests
import csv

with open('C:/Users/tarek/Desktop/acs.txt') as f:
    c = f.readlines()

acs = [x.strip() for x in c]
splits_t = []
ratios_t = []

for ac in acs:
    splits_t.append(ac)
    ratios_t.append(ac)
    url = 'https://finance.yahoo.com/quote/' + ac +'.SA/history?period1=946864800&period2=1519527600&interval=div%7Csplit&filter=split&frequency=1d'

    r = requests.get(url)
    p = soup(r.content,'html.parser')

    try:
        c = p.findAll('table',{'class':'W(100%) M(0)'})[0]
        td = c.findAll('td')        

        for i in range(0,len(td),2):
            if not '*' in td[i].span.text and not 'No Split' in td[i].span.text:
                splits_t.append(td[i].span.text)
                ratios_t.append(" " + td[i+1].strong.text)

        splits_t.append('')
        ratios_t.append('')

    except:
        splits_t.append('')
        ratios_t.append('')
        pass

with open('splits.csv', 'a', newline='', encoding='utf8') as f:
    w = csv.writer(f, delimiter=',')
    for i in range(len(splits_t)):
        w.writerow([splits_t[i], ratios_t[i]])