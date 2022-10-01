import csv
from numpy import product
import pandas as pd

product = pd.read_csv('dummyProduct.csv')
print(product)

recipe = pd.read_csv('dummyRecipe.csv')
print(recipe)

sold = pd.read_csv('dummySold.csv')
print(sold)

with open('dummySold.csv') as file_obj:
      
    # Create reader object by passing the file 
    # object to reader method
    reader_obj = csv.reader(file_obj)
      
    # Iterate over each row in the csv 
    # file using reader object
    for row in reader_obj:
        print(row)