import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import re

# data
prov = pd.read_csv("resources/COVID-19/dati-province/dpc-covid19-ita-province.csv")
prov['data'] = pd.to_datetime(prov['data']).dt.round('d')
prov['totale_casi'] = prov['totale_casi'].astype('int')

prov.loc[prov['denominazione_provincia']=='Napoli', 'sigla_provincia']="NA"
# prov['data'] = pd.to_datetime(prov['data'])
# prov['data'] = prov['data'].dt.strftime('%d-%m')
sns.lineplot(x='data', y='totale_casi', data=prov[prov['sigla_provincia']=='NA'])
plt.show()
fig = sns.lineplot(x='data', y='totale_casi', data=prov[prov['sigla_provincia']=='NA'])

fig.figure.savefig('output.png')
