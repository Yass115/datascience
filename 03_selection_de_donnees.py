import pandas as pd
df = pd.read_csv("data.csv")

print(df["email"].head()) # permet de récuperer les 5 premieres données de la colonne email
print("---------------------------------------------------------------------------------")
print(df.email.head()) # 2e façon de réecrire ce qui a été vu plus haut
print("-------------------------------------------------------------------------------")
print(type(df))
print(type(df.email)) # certaines méthodes s'utillisent QUE sur des dataframes et d'autres QUE sur des series (colonnes dans les dataframes)
print("---------------------------------------------------------")
print(df[10:20]) # on récupère les données de la 10e ligne (row) jusqu'a la 19e ligne (car exclusif)
print("------------------------------------------------------------------------------")
print(df.loc[10:13]) # on récupere (affiche) les données en partant de l'index 10 jusqu'a l'index 13 inclus
print("-----------------------------------------------------------------------------")
df_email = df.set_index("email")
print(df_email.loc['hharridge1@gnu.org']) # on récupère (affiche) les données liée au mail hharridge1@gnu.org
print("------------------------------------------------------------------------------------")
print(df_email.loc['hharridge1@gnu.org'].values) # récupere les données liée à ce mail et les mets dans une array
print("--------------------------------------------------------------------------")
print(df_email.loc[["ekilminster2@etsy.com", "hharridge1@gnu.org"]]) #pour récuperer les données de plusieurs emails on passe en paramètre une liste avec tous les emails
# df_email deviens un dataframe
print("-------------------------------------------------------------------")
