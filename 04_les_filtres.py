import pandas as pd
df = pd.read_csv("data.csv")

print(df["gender"]) #on récupere QUE la colonne "gender"
print("----------------------------------------------")
Male_filter = df["gender"] == "Male" #il s'agit d'un filtre/////renvoi un boolean true si la valeur est égale à male
print(df[Male_filter])
# si on fait le calcul des rows(lignes) que l'on a pour les males et females on aura pas 1000 car certaines lignes étaient non renseignées
print("---------------------------------------------------------------------------------")
country_filter = df["country"].isin(["France","Canada"]) #l'opérateur in n'existe pas dans pandas, à la place on utilise la méthode isin()
print(df[country_filter])
#vérifie quelles rows ont la valeur france ou canada
print("-------------------------------------------------------------------")
#filtre sur le prix (le prix ici c'est une chaine de caractère et pas un nombre)
#on peut pas comparer une chaine de caractère et un nombre
df_test = df.copy() #on copie le dataframe
df_test.price_paid = df_test.price_paid.apply(lambda x: x.replace("$", "")) #j'applique une fonction lambda qui va remplacer la chaine de caractère "$" par une chaine vide ""
df_test.price_paid = df_test.price_paid.astype(float) #une fois débarassé du $ on transforme la chaine de caractère du chiffre en un vrai chiffre de type float
price_filter = df_test["price_paid"] >= 5.0
print(df[price_filter]) #on récupère toutes les valeurs supérieures à 5.0