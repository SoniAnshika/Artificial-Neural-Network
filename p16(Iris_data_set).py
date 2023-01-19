import numpy as np
from sklearn.datasets import load_iris
iris=load_iris()

def pred(inp,w):
    if sum(inp*w)>0:
        return 1
    else:
        return 0

x=iris.data[:,(2,3)]
y=(iris.target==0).astype(np.int64)


def learning(x,y,w):
    print("\nWeight ",w)
    for epoch in range(10):
        print('----iterations ',epoch+1)
        for i,j in zip(x,y):
            if j-pred(i,w)<0:
                w=w-0.001*i
            elif j-pred(i,w)>0:
                w=w+0.001*i
            else:
                a=1
    return w
        
np.random.seed(11)
w=np.random.randn((len(x[0])))
w=learning(x,y,w)

#Test
print("\nTest.........")
print('Test instance 1= ',pred(x[1],w)==y[1])
print('Test instance 10= ',pred(x[10],w)==y[10])
print('Test instance -1= ',pred(x[-1],w)==y[-1])

#Accuracy
correct,incorrect=0,0
for i,j in zip(x,y):
    if pred(np.array(i),w)==j:
        correct+=1
    else:
        incorrect+=1
accuracy=(1.0*correct)/len(x)
print('accuracy= ',accuracy*100,'%')
