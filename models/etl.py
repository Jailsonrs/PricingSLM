import pandas as pd 
import numpy as np
import statsmodels

df = pd.read_csv("DATA/raw/products.csv",sep=";")

<<<<<<< HEAD
print(df.head(10))

df.info()
=======
#print(df.head(10))

#df.info()
>>>>>>> 0d06222 (models and utils)


#obtendo somente colunas necessarias
# criar variavel sintética de data de compra 
# extrair ano, semana, trimestre.
# simular demanda diária => derivar a partir dessas a demanda para semana, trimestre etc...
<<<<<<< HEAD
#modelar.
=======
#modelar.

train_cols = ['PRODUTO',"CLASSE TERAPÊUTICA","LABORATÓRIO","TARJA","PMC Sem Imposto","PMC 0%","PMC 12%","PMC 18%","PMC 21%","PMC 22%"]

df_train = df[train_cols]


df_train.dropna(inplace=True)
#print(df_train.isna().sum())
#print(df_train.describe())
#print(df_train.head(10))

#df_train[["PMC 12%"]].apply(lambda x: x.astype(float))
pmc_columns = ["PMC 12%", "PMC 18%", "PMC 21%", "PMC 22%"]  # List of target columns
df_train[pmc_columns] = df_train[pmc_columns].apply(lambda col: col.str.replace(r"[^\d.]", "", regex=True).astype(float))

print(df_train.info())


# Step 1: Generate date range
date_range = pd.date_range(start="2023-01-01", end="2024-12-31", freq="D")

# Step 2: Create a cartesian product of products and dates
products = df_train["PRODUTO"].unique()
expanded_data = pd.MultiIndex.from_product([products, date_range], names=["PRODUTO", "DATE"]).to_frame(index=False)

# Step 3: Merge with original product data
df_expanded = expanded_data.merge(df_train, on="PRODUTO", how="left")

# Step 4: Add synthetic QUANTITY_SOLD column


np.random.seed(42)  # For reproducibility
df_expanded["QUANTITY_SOLD"] = np.random.exponential(1, 50, size=len(df_expanded))  # Random quantity between 1 and 50

np.random.exponential()
df_expanded["UNITARY_PRICE"] = df_expanded.apply(
    lambda row: np.random.uniform(row["PMC 0%"], row["PMC 22%"]), axis=1
)

# Display the result
print(df_expanded.head())

df_expanded.to_csv("DATA/processed/synthetic_sales_expanded.csv", index=False)   



>>>>>>> 0d06222 (models and utils)
