import numpy as np

x = np.array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
y = np.array([0,0,0,0,0,0,0,1])


def pred(x,w):
    return 1 if sum(x*w) > 2 else 0

def learning(x,y,w):
    print('weight ',w)
    for k in range(1000):
        print('------iteration ',k+1)
        for i,j in zip(x,y):
            if j - pred(i,w) > 0:
                w = w + 0.01* i
            elif j - pred(i,w) < 0:
                w = w - 0.01* i
            else:
                a=1
    return w

np.random.seed(1)
w=np.random.randn((len(x[0])))
w = learning(x,y,w)

#Testing on training data
print('Test on training data.....')
for i,j in zip(x,y):
    print(pred(i,w)==j)

correct,incorrect =0,0
for i,j in zip(x,y):
    if pred(i,w)==j:
        correct += 1
    else:
        incorrect += 1
accuracy =(1.0* correct)/len(x)
print('accuracy = ',accuracy*100,'%')
