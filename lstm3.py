import pennylane as qml
from pennylane import numpy as np
from pennylane.optimize import AdamOptimizer
import matplotlib.pyplot as plt
#import numpy as np
import pylab
import matplotlib as mpl
import pandas as pd
data = np.loadtxt("sine.txt")
X = np.array(data[:, 0], requires_grad=False)
Y = np.array(data[:, 1], requires_grad=False)
print(X)
print(Y)

'''
df = pd.read_csv("27.5479_82.6384.csv")
print(df['date'][:10].tolist())
qml.about()
#data = np.loadtxt("sine.txt")
#X = np.array(data[:, 0], requires_grad=False)
#Y = np.array(data[:, 1], requires_grad=False)
dev = qml.device("strawberryfields.fock", wires=1, cutoff_dim=10)
def layer(v):
    # Matrix multiplication of inputs
    qml.Rotation(v[0], wires=0)
    qml.Squeezing(v[1], 0.0, wires=0)
    qml.Rotation(v[2], wires=0)

    # Bias
    qml.Displacement(v[3], 0.0, wires=0)

    # nonlinear transformation
    qml.Kerr(v[4], wires=0)
@qml.qnode(dev)
def quantum_neural_net(var, x=None):
    # Encode input x into a quantum state
    qml.Displacement(x, 0.0, wires=0)

    #call layer(v) which will be the subcircuit of the variational circuit of the neural network
    for v in var:
        layer(v)

    return qml.expval(qml.X(0))
def square_loss(labels, predictions):
    loss = 0
    for l, p in zip(labels, predictions):
        loss = loss + (l - p) ** 2

    loss = loss / len(labels)
    return loss
def cost(var, features, labels):
    preds = [quantum_neural_net(var, x=x) for x in features]
    return square_loss(labels, preds)
np.random.seed(0)
num_layers = 4
var_init = 0.05 * np.random.randn(num_layers, 5)
print(var_init)
opt = AdamOptimizer(0.01, beta1=0.9, beta2=0.999)

var = var_init
for it in range(500):
    var, _cost = opt.step_and_cost(lambda v: cost(v, X, Y), var)
    print("Iter: {:5d} | Cost: {:0.7f} ".format(it, _cost))
x_pred = np.linspace(-1, 1, 50)
predictions = [quantum_neural_net(var, x_) for x_ in x_pred]
plt.figure()
plt.scatter(X, Y)
plt.scatter(x_pred, predictions, color="green")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.tick_params(axis="both", which="major")
plt.tick_params(axis="both", which="minor")
plt.show()
'''    

