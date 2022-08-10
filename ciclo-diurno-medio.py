# autora: beatriz miranda
# data: 10/08/2022
# forma simples para calculo do ciclo diurno médio de mais de uma variavel
# dado-exemplo.csv está disponivel no diretorio

# biblioteca necessaria
import pandas as pd

df = pd.read_csv('.../dado-exemplo.csv',na_values='NaN',sep=';',index_col=0)

# agrupa os dados a partir da coluna 'HORA' presente no arquivo dado-exemplo
group_HORA = df.groupby('HORA')

# calcula a média para cada hora 
CDM = group_HORA.mean()

# salvando em um arquivo csv
CDM.to_csv('CDM.csv')
