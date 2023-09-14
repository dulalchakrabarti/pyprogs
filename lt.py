import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('sine.txt')
print(data.shape)
X = np.array(data[:, 0])
Y = np.array(data[:, 1])
plt.scatter(X,Y)
plt.show()

