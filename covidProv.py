import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# data
prov = pd.read_csv("resources/COVID-19/dati-province/dpc-covid19-ita-province.csv")
prov['data'] = pd.to_datetime(prov['data']).dt.round('d')
prov['totale_casi'] = prov['totale_casi'].astype('int')
dates = ['02/26', '02/27', '02/28', '02/29', '03/01', '03/02', '03/03', '03/04', '03/05', '03/06', '03/07', '03/08', '03/09', '03/10', '03/11', '03/12', '03/13', '03/14', '03/15', '03/16', '03/17', '03/18', '03/19', '03/20', '03/21', '03/22', '03/23', '03/24', '03/25', '03,26', '03/27', '03/28', '03/29', '03/30', '03/31']
prov.loc[prov['denominazione_provincia'] == 'Siracusa', 'sigla_provincia'] = "SR"
sns.lineplot(x='data', y='totale_casi', data=prov[prov['sigla_provincia'] == 'SR'])
latus = plt.xticks()
plt.xticks(latus[0], dates)
plt.show()
fig = sns.lineplot(x='data', y='totale_casi', data=prov[prov['sigla_provincia'] == 'SR'])
latus = plt.xticks()
plt.xticks(latus[0], dates)
fig.figure.savefig('output.png')
