import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import re

# data
prov = pd.read_csv("resources/COVID-19/dati-province/dpc-covid19-ita-province.csv")
prov['data'] = pd.to_datetime(prov['data']).dt.round('d')
prov['totale_casi'] = prov['totale_casi'].astype('int')
dates = ['02/26', '02/27', '02/28', '02/29', '02/26', '02/26', '02/26', '02/26', '02/26']
prov.loc[prov['denominazione_provincia']=='Napoli', 'sigla_provincia']="NA"
# prov['data'] = pd.to_datetime(prov['data'])
# prov['data'] = prov['data'].dt.strftime('%d-%m')
sns.lineplot(x='data', y='totale_casi', data=prov[prov['sigla_provincia']=='NA'])
l = plt.xticks()
plt.xticks(l[0], dates)
plt.show()
fig = sns.lineplot(x='data', y='totale_casi', data=prov[prov['sigla_provincia']=='NA'])
l = plt.xticks()
plt.xticks(l[0], dates)
fig.figure.savefig('output.png')