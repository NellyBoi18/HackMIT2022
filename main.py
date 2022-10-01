from numpy import product
import pandas as pd



<<<<<<< HEAD
sold = pd.read_csv('dummySold.csv')
print(sold)
sold.columns
=======
product = pd.read_csv('dummyProduct.csv',index_col=0)
recipe = pd.read_csv('dummyRecipe.csv',index_col=0)
sold = pd.read_csv('dummySold.csv',index_col=0)


p=sold.loc["burger"]
print(p)
>>>>>>> 41c7fa7dfc2b44594857d2365ca365519e58eb9d
