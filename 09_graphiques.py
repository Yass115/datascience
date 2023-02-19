import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

print(df.dropna(subset=["tax"], inplace=True))
df.price_paid = df.price_paid.apply(lambda x: x.replace("$", ""))
df.price_paid = df.price_paid.astype(float)
print(df.dtypes)
df["price_total"] = df["price_paid"] * (1 - df["tax"] / 100)
print(df["tax"].fillna(0,inplace=True))
print("---------------------------------------------------------------------")
df.drop(["first_name", "last_name", "email", "ip_address", "id"], axis=1, inplace=True)
print("---------------------------------")

prix_total = df.groupby("date")["price_paid"].sum()#afficher pour chaque jour du mois le prix total qui a été payé par les gens dans le dataframe
print(prix_total)

#pour l'afficher en graphique on écrit:
#prix_total_graphe = df.groupby("date")["price_paid"].sum().plt(figsize=[20, 10]) #avec cette syntaxe là on peut afficher le graphique sur jupyterlab
#print(prix_total_graphe)
print("--------------------------------------------")

#afficher le graphique sur pycharm
plt.plot(prix_total)# on peut utiliser la méthode plot sur n'importe quels données
plt.show()

#graphique en camambert
#gender_prop = df.groupby("gender")["price_paid"].sum().plot.pie() #sur jupyterlab

gend = df.groupby("gender")["price_paid"].sum()
graph = plt.pie(gend)
plt.show()

#histogramme
#df.groupby("country")["price_paid"].sum().plt.bar(rot=45,legand=True) syntaxe sur jupyterlab
prix_paye_par_chaque_pays = df.groupby("country")["price_paid"].sum()
plt.bar(prix_paye_par_chaque_pays,height=3,width=20)
plt.show()



