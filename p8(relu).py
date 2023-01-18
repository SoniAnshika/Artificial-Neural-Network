import numpy as np

n=int(input("Enter the number of neurons in the hidden layer: "))

inputs=[]
num=int(input("Number of Inputs: "))
print("Enter the inputs: ")
for i in range(0,num):
    x=int(input())
    inputs.append(x)

def percept(n,inputs):
    Ohp=[]
    c=0
    np.random.seed(52)
    wts=np.random.randn(n*num)
    print("Weights of Hidden Layer: ",wts)
    for i in range(0,n):
        o=0
        for j in range(0,num):
            o=o+wts[c]*inputs[j]
            c=c+1
        m1=max(0,o)
        Ohp.append(m1)
    print("Outputs of Hidden Layer: ",Ohp)
    y=0
    np.random.seed(52)
    Wts=np.random.randn(n)
    print("Weights of Output Layer: ",Wts)
    for i in range(0,n):
        y=y+Wts[i]*Ohp[i]
    m2=max(0,y)
    
    return m2

Y=percept(n,inputs)
print("Output: ",Y)
