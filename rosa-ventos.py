# script para plot da rosa dos ventos baseado no passo a passo do site meteopassos 
# http://www.meteopassos.com/como-fazer-uma-rosa-dos-ventos-em-python
# contem um loop para plot da rosa dos ventos de mais de uma estacao de qualidade do ar do  inea
# dados organizados utilizando o script sel-dados-rosa-ventos

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from windrose import WindroseAxes, WindAxes, plot_windrose

lista_nomes = ['São Bernardo','Jardim Primavera','Pilar',
               'São Bento','Vila São Luiz','Monteiro Lobato',
               'Engenheiro Pedreira','Jardim Guandu',
               'Campo dos Afonsos','Lagoa','Ilha de Paquetá',
               'Ilha do Governador','Leblon','Maracanã','Taquara',
               'Urca','Adalgisa Nery','UERJ','Piranema','Largo do Bodegão']
               
e = 0
while e < len(lista_nomes): #para cada estacao
    x = lista_nomes[e]
    xstr = str(x)
    arquivo = '.../'+xstr+'-vento_aug-2016.csv'
    df = pd.read_csv(arquivo,na_values='NaN',sep=',')
    df.columns = ['date','Dir','Int']
    
    #Definindo o tamanho da fonte para os labels N, N-E, E, etc..., 
    # e também aumenta o título da legenda
    plt.rcParams["font.size"] = 18  
    
    #Criando o eixo da rosa dos ventos
    ax = WindroseAxes.from_ax()
    
    #Plotando os dados
    ax.bar(df.Dir, df.Int,normed=True, bins=np.arange(0,10,2), opening=0.8, edgecolor='white')
    
    #Inserindo a legenda 
    #(loc se refere à posição da legenda)
    #Shadow=False para que a caixa da legenda não tenha sombra
    lgd = ax.set_legend(title='Vel. do Vento (m.s⁻¹)', loc=(1.1, 0), shadow=False)
    
    # Aumenta o texto da legenda
    plt.setp(lgd.get_texts(), fontsize=16) 
    
    #Definindo quais vão ser os ticks(linhas cinza no gráfico)
    ax.set_yticks(np.arange(0, 20, step=4))
    
    #Inserindo os labels no eixo
    ax.set_yticklabels(np.arange(0, 16, step=4), fontsize='14')
    
    #Inserindo o título do gráfico
    plt.title('August - '+xstr+'', y=1.08, fontsize='20')
    
    #Salvando a Rosa dos ventos
    plt.savefig('.../'+xstr+'-rosa-ventos-aug.jpg',bbox_inches='tight')
    e = e + 1 #passa para a proxima estacao
