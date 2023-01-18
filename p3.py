n=int(input("Enter the number of neurons in the hidden layer: "))

inputs=[]
num=int(input("Number of Inputs:"))
print("Enter the inputs:")
for i in range(0,num):
    x=int(input())
    inputs.append(x)
print("Inputs are: ",inputs)

wts=[]
print("Enter the weights of hidden layer:")
for i in range(0,num*n):
    w=int(input())
    wts.append(w)
print("Hidden Layer Weights are: ",wts)


Wts=[]
print("Enter the weights of output layer:")
for i in range(0,n):
    W=int(input())
    Wts.append(W)
print("Output Layer Weights are: ",Wts)

def percept(n,inputs,wts,Wts):
    Ohp=[]
    c=0
    for i in range(0,n):
        o=0
        for j in range(0,num):
            o=o+wts[c]*inputs[j]
            c=c+1
        Ohp.append(o)
    print("Outputs of Hidden Layer: ",Ohp)

    y=0
    for i in range(0,n):
        y=y+Wts[i]*Ohp[i]

    print("Output: ",y)

percept(n,inputs,wts,Wts)
