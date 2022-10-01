import csv
from numpy import product
import pandas as pd

product = pd.read_csv('dummyProduct.csv')
print(product.to_string())
