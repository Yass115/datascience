import pandas as pd
df = pd.read_csv("data.csv")

print(df.dropna(subset=["tax"], inplace=True))
df.price_paid = df.price_paid.apply(lambda x: x.replace("$", ""))
df.price_paid = df.price_paid.astype(float)
print(df.dtypes)
df["price_total"] = df["price_paid"] * (1 - df["tax"] / 100)
print(df["tax"].fillna(0,inplace=True))
print("---------------------------------------------------------------------")
df.drop(["first_name", "last_name", "email", "ip_address", "id"], axis=1, inplace=True)
print(df)
print("----------------------------------------")
print(df.describe()) # nombres de données dans chaque colonne et leurs chiffres (moyenne max,min,etc)
mean = df["price_total"].mean()
print(f"la moyenne des valeurs de la colonne du prix total est de {mean}") #pour faire la moyenne arithmétiue de price_total
sum = df["price_total"].sum()
print(f"la somme des valeurs du prix total est de {sum}") #en faire la somme
min = df["price_total"].min()
max = df["price_total"].max()
print(f"la valeur max est de {max}")
print(f"la valeur min est de {min}")
unique_values = df["country"].unique().tolist() #voir toutes les valeurs "uniques" (valeurs possibles que l'on retrouve dans la colonne ou meme dans le dataframe tout entier)
print(f"les valeurs uniques dans le colonne country sont: {unique_values}")
print("----------------------------")
counts = df["country"].value_counts() #nombre de fois qu'une valeur apparait dans country
print(counts)

gender = df["gender"].value_counts(normalize=True) #pour avoir un pourcentage plutot que des chiffres
print(gender)

print(df.groupby("price_total").sum()) #on peut retrouver la somme de tous les prix par pays (on peut appliquer groupby à d'autres colonnes)
print(df.groupby("country").mean()) ##voir quel est le pays qui est le mieux payé en moyenne
print(df.groupby("gender")["price_paid"].mean()) #voir en moyenne les femmes combien elles payent et les hommes combien ils payent
print(df.groupby(["gender", "country"]).mean()) #tableau à double entré pour voir combien les femmes payent par pays / ou hommes

