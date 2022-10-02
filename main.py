from numpy import product
import numpy as np
import pandas as pd
from sympy import re

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
    remaining=pd.DataFrame()
    remaining["Food_Waste"]=inventoryDF["Count"]-used["sum"]
    remaining["Cost_of_Waste"]=remaining["Food_Waste"]*inventoryDF["Unit Price"]
    return remaining

remaining = calculating("dummyProduct.csv","dummyRecipe.csv","dummySold.csv")

Jan = calculating("dummyProduct.csv","dummyRecipe.csv","dummySold.csv")
Feb = calculating("dummyProduct2.csv","dummyRecipe.csv","dummySold2.csv")
Mar = calculating("dummyProduct3.csv","dummyRecipe.csv","dummySold3.csv")

monthRemaining = pd.concat([Jan.T[0:1], Feb.T[0:1], Mar.T[0:1]])
monthRemaining = monthRemaining.rename_axis("Month", axis="columns")
monthRemaining = monthRemaining.set_axis(['Jan', 'Feb', 'Mar'], axis=0)
#monthRemaining.insert(0, 'index', [*range(len(monthRemaining))])
print(monthRemaining)