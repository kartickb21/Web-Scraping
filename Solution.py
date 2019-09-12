import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get("http://marvel-ironman.surge.sh")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

#1st data in h4
#fname = soup.find_all('h2')
#fdata = soup.find_all('h4')

names = soup.select('h2, p.h2')#, 'p.h2'])
data = soup.select('h4, p.h4')
#names = soup.find_all('p', class_='h2')
#data = soup.find_all('p', class_='h4')
l = []
'''for i in fname:
    l.append(i.getText())'''
for i in names:
    l.append(i.getText())


x = []
'''for i in fdata:
    x.append(i.getText())'''
for i in data:
    x.append(i.getText())   

year = []
iden = []
align = []
eye = []
hair = []
sex = []
alive = []
app = []
fapp = []
for i in x:
    if "Year" in i:
        year.append((i.split(':')[1]).strip())
    if "Identity" in i:
        iden.append((i.split(':')[1]).strip())
    if "Align" in i:
        align.append((i.split(':')[1]).strip())
    if "Eye" in i:
        eye.append((i.split(':')[1]).strip())
    if "Sex" in i:
        sex.append((i.split(':')[1]).strip())
    if "Hair" in i:
        hair.append((i.split(':')[1]).strip())
    if "Alive" in i:
        alive.append((i.split(':')[1]).strip())
    if "Appearances" in i:
        app.append((i.split(':')[1]).strip())
    if "First Appearance" in i:
        fapp.append((i.split(':')[1]).strip())
        
df = pd.DataFrame(columns=['name','id','align','eye','hair','sex','alive','appearances','first appearance','year'])
df['name'] = l
df['id'] = iden
df['align'] = align
df['eye'] = eye
df['hair'] = hair
df['sex'] = sex
df['alive'] = alive
df['appearances'] = app
df['first appearance'] = fapp
df['year'] = year

xd = df.replace('None','')
xd.to_csv('data.csv', index=False)