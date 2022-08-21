import pandas as pd
import numpy as np

arquivo = '.../dado_wind_u_v.csv'
df = pd.read_csv(arquivo,sep='\t',index_col=0)
        
#velocidade/intensidade do vento:
# formula -> intensidade = (u²+v²)¹/²
u_quadrado = pow(df['u'],2)
v_quadrado = pow(df['v'],2)
df['Intensidade'] = pow((u_quadrado+v_quadrado),0.5)

#direcao do vento:
# formula -> direção = arctan2(u,v) * 180/pi
direcao = (np.arctan2(df['u'],df['v'])) * 180/np.pi

#convenção meteorológica da direção de onde o vento está vindo
direcao_from_degrees = direcao + 180
df['Direção'] = direcao_from_degrees
print(df)
