import csv
from numpy import product
import pandas as pd

print("test push")

product = pd.read_csv('dummyProduct.csv',index_col=0)
recipe = pd.read_csv('dummyRecipe.csv',index_col=0).transpose()
sold = pd.read_csv('dummySold.csv',index_col=0).transpose()
rec=list(recipe.columns)
used=pd.DataFrame()
for i in rec:
    prod=sold[i]
    used[i]=recipe[i]*prod[0]
used["sum"] = used.sum(axis=1)
remaining=product["Count"]-used["sum"]
print(remaining)