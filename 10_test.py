import pandas as pd
from matplotlib import *

#traitement de la colonne type
df = pd.read_csv("netflix_titles.csv")
nbre_type = df["type"].value_counts(normalize=True) *100
print(nbre_type)
print("--------------------------------------------------------------------")

country = df["country"]
country_filter = df["country"].isin(["France","Belgium"])
print(country_filter)
# je vous laisse continuer l'analyse de ces données Netflix qui sont opensource
