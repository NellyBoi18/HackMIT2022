from main import *
import matplotlib.pyplot as plt



product = list(remaining.index)
print(product)
quantity = list(remaining.values)
print(quantity)

# Single month food waste
fig = plt.figure(figsize = (10, 5))
plt.bar(product, quantity, color = 'blue', width = 0.2)
plt.show()


# Multiple month food waste
monthRemainingData = {}
for month in data:
   monthRemainingData[month] = list(data.values)

'''
plt.bar(x, y1, color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
plt.bar(x, y1+y2, ccolor=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
plt.show
'''