import numpy as np

x=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([[0],[1],[1],[1]])

w1=np.random.randint(-10,10)
w2=np.random.randint(-10,10)

def TLU(inp,w):
    if sum(inp*w)>0:
        return 1
    else:
        return 0


print("Initial Value of w1 and w2: ",w1,end=" ")
print(w2,end="\n\n")

for epoch in range(15):
    for i,j in zip(x,y):
        if j==1 and TLU(i,[w1,w2])==0:
            w1=w1-1
            w2=w2-1
        elif j==0 and TLU(i,[w1,w2])==1:
            w1=w1+1
            w2=w2+1
        
    print('epoch=',epoch+1)
    print("Value of w1 and w2: ",w1,end=" ")
    print(w2,end="\n\n")

print("Final Value of w1 and w2: ",w1,end=" ")
print(w2)
