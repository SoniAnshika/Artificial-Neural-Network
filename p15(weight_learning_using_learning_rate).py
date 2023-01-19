import numpy as np

def TLU(inp,w):
    if sum(inp*w)>0:
        return 1
    else:
        return 0

def learning(x,y,w):
    print("\nWeight ",w)
    for epoch in range(15):
        print('----iterations ',epoch+1)
        for i,j in zip(x,y):
            if j[0]-TLU(i,w)<0:
                w=w-1*i
            elif j[0]-TLU(i,w)>0:
                w=w+1*i
    return w
        
x=np.array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
y=np.array([[0],[1],[1],[1],[1],[1],[1],[1]])
w=np.random.randn((len(x[0])))
w=learning(x,y,w)

#Test
print("\nTest.........")
for i in x:
    print(TLU(i,w))
