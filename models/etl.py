import pandas as pd 
import numpy as np
import statsmodels

df = pd.read_csv("DATA/raw/products.csv",sep=";")

print(df.head(10))

df.info()


#obtendo somente colunas necessarias
# criar variavel sintética de data de compra 
# extrair ano, semana, trimestre.
# simular demanda diária => derivar a partir dessas a demanda para semana, trimestre etc...
#modelar.