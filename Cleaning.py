import pandas as pd

data = pd.read_csv('data.csv')
data = data.fillna('not-available')

#data = data['timeline']
x = list(data['first appearance'])
y = []
for i in x:
    y.append(i.split('-')[0])

'''year = list(data['year'])
z = []
for i,j in y,year:
    z.append(i+j)'''

data['month'] = y
data['timeline'] = "01/"+data['month']+"/"+data['year'].astype(str)
z = list(data['timeline'])
k = []
for i in z:
    k.append(i.split('.')[0])
data['timeline'] = k 
data['timeline'] = pd.to_datetime(data['timeline'], errors='coerce')
data['timeline'] = data['timeline'].dt.strftime('%Y-%m-%d') 

data = data.replace('NaT','not-available')
data = data.drop(columns = ['first appearance', 'year', 'month'])
data.to_csv('cleaned_data.csv', index=False)

#data = data.set_index('timeline')
#1st Jan 1975 to 1st Aug 2015
#datax = data[data['index'].between('1975-01-01', '2015-01-01')]
datax = data[(data['timeline'] > '1975-01-01') & (data['timeline'] <= '2015-01-01')]
names = datax['name']
names = sorted(names)
namedf =  pd.DataFrame(names)
namedf.to_csv('names.csv',index=False, header=False)