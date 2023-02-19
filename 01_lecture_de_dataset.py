#on utilise souvent des fichiers csv (comma separated values)
import pandas as pd
df = pd.read_csv("data.csv") # df pour dataframe = tableau entier de donnée contrairement au type series qui ne sont qu'une colonne ou ligne dans le tableau
print(df)