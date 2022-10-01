import csv
from numpy import product
import pandas as pd

def calculating(inventory,recipe,sold):
    inventoryDF = pd.read_csv(inventory,index_col=0)
    recipeDF = pd.read_csv(recipe,index_col=0).transpose()
    soldDF = pd.read_csv(sold,index_col=0).transpose()
    rec=list(recipeDF.columns)
    used=pd.DataFrame()
    for i in rec:
        prod=soldDF[i]
        used[i]=recipeDF[i]*prod[0]
    used["sum"] = used.sum(axis=1)
    remaining=inventoryDF["Count"]-used["sum"]
    return remaining
print(calculating("dummyProduct.csv","dummyRecipe.csv","dummySold.csv"))