import numpy as np
import matplotlib.pyplot as plt

def tanh(x):
    return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

def d_tanh(x):
    return (4*np.exp(-x)*np.exp(x))/((np.exp(x)+np.exp(-x))*(np.exp(x)+np.exp(-x)))

x=np.linspace(-10,10)
plt.plot(x,tanh(x),'blue',label='tanh')
plt.plot(x,d_tanh(x),'red',label='derivative of tanh')
plt.legend()
plt.show()
