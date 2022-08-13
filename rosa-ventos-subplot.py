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
    
    #abrindo arquivos de dado separados por meses para cada estacao
    arquivo1 = '.../'+xstr+'-vento_aug-2016.csv'
    df1 = pd.read_csv(arquivo1,na_values='NaN',sep=',')
    df1.columns = ['Date','Dir','Int']
    
    arquivo2 = '.../'+xstr+'-vento_sep-2016.csv'
    df2 = pd.read_csv(arquivo2,na_values='NaN',sep=',')
    df2.columns = ['Date','Dir','Int']
       
    #uma linha e duas colunas
    nrows, ncols = 1, 2
    fig = plt.figure(figsize=(20, 20))
    #ajusta  o espaco entre os subplots e o titulo
    plt.subplots_adjust(wspace = 0.6,top = 1.37)
    fig.tight_layout()
    plt.rcParams["font.size"] = 18  
    #titulo da figura
    fig.suptitle(''+xstr+'',fontweight='bold',fontsize=23)
    
    #plot 1:
    ax1 = fig.add_subplot(nrows, ncols, 1, projection="windrose")
    #Plotando os dados
    ax1.bar(df1.Dir, df1.Int, normed=True, bins=np.arange(0,10,2), opening=0.8, edgecolor='white')
    #legenda
    lgd1 = ax1.set_legend(title='Vel. do Vento (m.s⁻¹)', loc=(1.1, 0), shadow=False)
    # Aumenta o texto da legenda
    plt.setp(lgd1.get_texts(), fontsize=16) 
    #Definindo quais vão ser os ticks(linhas cinza no gráfico)
    ax1.set_yticks(np.arange(0, 20, step=4))
    #Inserindo os labels no eixo
    ax1.set_yticklabels(np.arange(0, 16, step=4), fontsize='14')
    plt.title('August', y=1.08, fontsize='20')

    #plot 2:
    ax2 = fig.add_subplot(nrows, ncols, 2, projection="windrose")
    #Plotando os dados
    ax2.bar(df2.Dir, df2.Int, normed=True, bins=np.arange(0,10,2), opening=0.8, edgecolor='white')
    lgd2 = ax2.set_legend(title='Vel. do Vento (m.s⁻¹)', loc=(1.1, 0), shadow=False)
    # Aumenta o texto da legenda
    plt.setp(lgd2.get_texts(), fontsize=16) 
    #Definindo quais vão ser os ticks(linhas cinza no gráfico)
    ax2.set_yticks(np.arange(0, 20, step=4))
    #Inserindo os labels no eixo
    ax2.set_yticklabels(np.arange(0, 16, step=4), fontsize='14')
    plt.title('September', y=1.08, fontsize='20')

    #Salvando a Rosa dos ventos
    plt.savefig('.../'+xstr+'-rosa-ventos.jpg', bbox_inches='tight')
    e = e + 1 #passa p proxima estacao