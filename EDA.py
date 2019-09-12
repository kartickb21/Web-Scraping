import pandas as pd


data = pd.read_csv('cleaned_data.csv')
datadup = data
data['timeline'] = pd.to_datetime(data['timeline'], format="%Y/%m/%d",  errors='coerce')
#d#ataback = data.copy()
#datax = data[(data['timeline'] > '1938') & (data['timeline'] < '1956')]
datax = data[(data['timeline'] > '1938-01-01') & (data['timeline'] <= '1956-12-01')]

#datax = datax[datab['timeline'].between('1938', '1956')]
#characters = list(datax['name'].unique())
#fans = len(characters)
fans = datax.shape[0]

datay = data[data['id'] == 'public identity']
datay = datay[(datay['timeline'] > '1956-01-01') & (datay['timeline'] <= '1970-12-01')]
chars = list(datay['name'].unique())
sans = len(chars)

dataz = datadup[datadup['eye'] == 'blue eyes']
dataz = dataz[dataz['sex'] == 'male characters']
blueeyez = dataz.shape[0]

datab = data[data['align'] == 'good characters']
datab = datab[datab['alive'] == 'living characters']
datab = datab[datab['id'] == 'secret identity']
tans = datab.shape[0]

datagood = data[data['align'] == 'good characters']
databad = data[data['align'] == 'bad characters']
gvb = abs(datagood.shape[0] - databad.shape[0])

datahw = data[data['timeline'].dt.month == 10]
fians = datahw.shape[0]

datain = data[data['timeline'].dt.year > 1970]
sixans = datain.shape[0]

dataalb = databad[databad['alive'] ==  'living characters']
medians = int(dataalb['appearances'].median())

datasec = data[data['id'] == 'secret identity']
mvw = (datasec[datasec['sex']== 'male characters']).shape[0] - (datasec[datasec['sex']== 'female characters']).shape[0]
if(mvw > 0 ):
    male = 'yes'

earth = list(data['name'])
n=0
for i in earth:
    if "earth-616" not in i:
        n = n+1
        
l = [fans, sans, blueeyez, tans, gvb, fians, sixans, medians, male, n]
key = ['ans_1','ans_2','ans_3','ans_4','ans_5','ans_6','ans_7','ans_8','ans_9','ans_10']
ansdf = pd.DataFrame()
ansdf['key']=key
ansdf['ans']=l
ansdf.to_csv('answer.csv', index=False)
