import pandas as pd 

df_train = pd.read_csv("DATA/processed/synthetic_sales_expanded.csv")
#print(df_train.sample(20))

print(df_train[['DATE']])