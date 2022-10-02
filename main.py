from numpy import product
import numpy as np
import pandas as pd
from sympy import re
import matplotlib.pyplot as plt

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

# Takes in a DataFrame object containing month and food waste per month
def linReg(df):

    # Lin reg for every ingredient
    columns = df.columns
    # Declaring x axis (months)
    x = [1, 2, 3] # Months

    print(x)

    # Y axis (waste)
    # yDF = pd.MultiIndex.from_frame(df["Waste"]) # Getting data from dataFrame inside dataFrame df
    # print(yDF)

    bunWaste = []
    bunWaste.append(df["Jan"]["bun"])
    bunWaste.append(df["Feb"]["bun"])
    bunWaste.append(df["Mar"]["bun"])
    print(bunWaste)

    coef = np.polyfit(x,bunWaste,1)
    poly1d_fn = np.poly1d(coef) # Function that takes in x and returns an extimate for y

    # Plotting
    plt.plot(x, bunWaste, 'yo', poly1d_fn(x), '--k') # 'yo' = yellow circle marker, '--k' = black dashed line
    plt.xlim(1,3)
    plt.show()


    pass # TEMP. Remove when done

remaining = calculating("dummyProduct.csv","dummyRecipe.csv","dummySold.csv")

Jan = calculating("dummyProduct.csv","dummyRecipe.csv","dummySold.csv")
Feb = calculating("dummyProduct2.csv","dummyRecipe.csv","dummySold2.csv")
Mar = calculating("dummyProduct3.csv","dummyRecipe.csv","dummySold3.csv")

monthRemaining = pd.concat([Jan.T[0:1], Feb.T[0:1], Mar.T[0:1]])
monthRemaining = monthRemaining.rename_axis("Month", axis="columns")
monthRemaining = monthRemaining.set_axis(['Jan', 'Feb', 'Mar'], axis=0)
#monthRemaining.insert(0, 'index', [*range(len(monthRemaining))])
print(monthRemaining.info())

# Testing linReg()
linRegXYData = pd.DataFrame()
#linRegXYData["Month"] = ([1], [2], [3])
linRegXYData["Jan"] = Jan["Food_Waste"]
linRegXYData["Feb"] = Feb["Food_Waste"]
linRegXYData["Mar"] = Mar["Food_Waste"]
print(linRegXYData)
linReg(linRegXYData)
