# a partir de um arquivo .csv contendo as informacaoes de direção e intensidade do vento para todas as estações, 
# o script separa e salva em um .csv as duas informações para cada uma das estacoes individualmente.  

import pandas as pd

df = pd.read_csv('.../ventos-obs-aug2016.csv',na_values='NaN',sep=';',index_col=0)

lista_nomes = ['São Bernardo','Jardim Primavera','Pilar',
               'São Bento','Vila São Luiz','Monteiro Lobato',
               'Engenheiro Pedreira','Jardim Guandu',
               'Campo dos Afonsos','Lagoa','Ilha de Paquetá',
               'Ilha do Governador','Leblon','Maracanã','Taquara',
               'Urca','Adalgisa Nery','UERJ','Piranema','Largo do Bodegão']
               
i = 1
j = 2
for estacao in lista_nomes:
    df1 = df.iloc[:,[i,j]]
    df1.to_csv('.../'+estacao+'-vento_aug-2016.csv')
    i = i + 2
    j = j + 2
