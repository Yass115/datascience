import pandas as pd
df = pd.read_csv("data.csv")

df.drop("ip_address", axis=1) #permet de supprimer une colonne (axe 1 = colonne///axe 0 = ligne row)
df.set_index("gender", inplace=True) #on met "gender" en tant qu'index
print(df)
print("------------------------------------------------------")
df.drop("Male", axis=0) # on supprime toutes les lignes qui sont spécifiés male
print(df)
print("---------------------------------------------------------------")
df.drop(["first_name","last_name","email"], axis=1, inplace = True) #supprimer plusieurs colonnes en meme temps
print(df)
print("------------------------------------------------------------------------------------")
del df["id"] #pas besoin de spécifier inplace, del le supprimera définitivement du dataset
print(df)
print("----------------------------------------------------------------------------")
