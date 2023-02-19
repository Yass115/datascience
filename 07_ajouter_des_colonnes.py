import pandas as pd
df = pd.read_csv("data.csv")

print(df.dropna(subset=["tax"], inplace=True)) #supprimer les valeurs nulles
print(df["tax"].fillna(0,inplace=True)) #remplacer les valeurs manquantes par 0
print("---------------------------------------------------------------------")
#on change le type des chiffres en chaines de caractère pour les transformer en float
df.price_paid = df.price_paid.apply(lambda x: x.replace("$", ""))
df.price_paid = df.price_paid.astype(float)
print(df.dtypes)
print("----------------------------------------")
df["price_total"] = df["price_paid"] * (1 - df["tax"] / 100)#on ajoute une colonne price_total et on y stock le prix calculé
print(df)
print("---------------------------------------------------------------------------")
countries = {"United States": "UN", "France": "FR", "Canada": "CA", "Morocco": "MA"} #dictionnaire pour mapper les valeurs entre elles (qu'est ce qu'on a envie de remplacer par quoi)
df["country_code"] = df["country"].map(countries) #nouvelles colonnes country_code ou l'on met les valeurs de country par les valeurs dans countries
print(df)
