from main import *
import matplotlib.pyplot as plt


product = list(Jan.iloc[:, 0].index)
print(product)
quantity = list(Jan.iloc[:, 0].values)
print(quantity)

# Single month food waste
fig = plt.figure(figsize = (10, 5))
plt.bar(product, quantity, color = 'blue', width = 0.2)
plt.show()


# Multiple month food waste

monthRemaining.plot(x='Month', kind='bar', stacked=True,
        title='Stacked Bar Graph by dataframe')
plt.show()
