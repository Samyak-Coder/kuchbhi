import pandas as pd
import csv

df = pd.read_csv("proejct\stars.csv")

df["Radius"] = 0.102763*len(df["Radius"])

#df['Mass']=df['Mass'].apply(lambda x: x.replace('$', ''))
df["Mass"] = 0.000954588*len(df["Mass"])

df.to_csv("ConvertedStars.csv")