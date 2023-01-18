import numpy as np

x1=[0,0,1,1]
x2=[0,1,0,1]
y=[0,1,1,1]
b=np.random.randn(1);

while(True):
    flag=True
    for i in range(0,4):
        o=x1[i]+x2[i]-b
        if o>=0:
            Y=1
        else:
            Y=0
        if y[i]!=Y:
            flag=False
            if y[i]>Y:
                b=b-1
                break
            else:
                b=b+1
                break

    if flag==True:
        break

for i in range(0,4):
    print("Input 1: ",x1[i])
    print("Input 2: ",x2[i])
    o=x1[i]+x2[i]-b
    print("Output: ",o)
    if o>=0:
        Y=1
    else:
        Y=0
    print("Actual Output: ",Y)
    print()

print("Final Threshold Value is: ",b)
            
            
                
            
            
        
        
