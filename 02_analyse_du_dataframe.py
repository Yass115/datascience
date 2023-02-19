import pandas as pd
df = pd.read_csv("data.csv")
print(df.head())  # permet d(afficher les 5 premieres lignes par défaut (on peut spécifier le nombre de lignes que nous voulons afficher, exemple df.head(9) pour les 9 premières lignes
print("------------------------------------------------------------------------------")
print(df.tail()) # meme chose que heaud() mais en commencant de la fin du tableau
print("--------------------------------------------------------------------------------------")
print(df.shape) # permet de connaitre la taille du dataframe
print("------------------------------------------------------------------------------------")
print(df.columns) # permet d'obtenir le titre des colonnes
print("-------------------------------------------------------------------------------------")
print(df.columns.tolist()) # cette fois ci en organisant les titres des colonnes dans une liste
print("------------------------------------------------------------------------------")
print(df.index) # afficher l'index (nbre d'elements dans dataframe
print("----------------------------------------------------------------")
print(df.set_index("email")) #la colonne "email" devient l'index mais ce n'est pas permanent / pour que ça soit permanent nous pouvons le stocker dans une variable ou bien utiliser le paramètre inplace = true
print("----------------------------------------------------------------------------------------")




