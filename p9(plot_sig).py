import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1.0/(1.0+np.exp(-x))

def d_sig(x):
    return (np.exp(-x))/((1+np.exp(-x))*(1+np.exp(-x)))

x=np.linspace(-10,10)
plt.plot(x,sigmoid(x),'blue',label='sigmoid')
plt.plot(x,d_sig(x),'red',label='derivative of sigmoid')
plt.legend()
plt.show()
