import pandas as pd
df = pd.read_csv("data.csv")

print(df.isnull()) # méthode qui me renvoi un boolean True si la valeur dans un endroit du tableau est nulle (manquante(NaN))
print("----------------------------------------------------------------")
print(df.notnull()) # fait l'inverse de isnull()
print("-----------------------------------------")
null_taxe_filtre = df["tax"].notnull()
print(df[null_taxe_filtre]) # filtre pour enlever toutes les taxes avec des valeurs nulles
print("--------------------------------------------------------------")
print(df["tax"].fillna(0)) # pour remplacer toutes les données non renseignées (NaN) par 0
print("----------------------------------------------------------------------------")
print(df["tax"].fillna(method="bfill")) # la méthode bfill permet de remplir les données NaN par les valeurs aux alentours de NaN
print("---------------------------------------------------------------------------------------")
print(df.dropna()) #méthode qui permet d'enlever toutes les données nulles
print("---------------------------------------------------------------------------------")
print(df.dropna(subset="tax", inplace=True)) #enleve toutes les valeurs nulles de la colonnes taxe (inplace=True permet de rendre la modification dudataframe permanente au lieu de stocker la modification dans une autre variable)

