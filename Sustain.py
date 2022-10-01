import csv
from numpy import product
import pandas as pd

product = pd.read_csv('dummyProduct.csv')
print(product)

recipe = pd.read_csv('dummyRecipe.csv')
print(recipe)

sold = pd.read_csv('dummySold.csv')
print(sold)