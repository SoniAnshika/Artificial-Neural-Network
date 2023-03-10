import numpy as np

class Perceptron(object):

    def __init__(self,no_of_inputs,threshold=10,learning_rate=0.1):
        self.threshold=threshold
        self.learning_rate=learning_rate
        self.weights=np.zeros(no_of_inputs+1)

    def predict(self,inputs):
        summation=np.dot(inputs,self.weights[1:])+self.weights[0]
        if summation>0:
            return 1
        else:
            return 0

    def fit(self,training_inputs,labels):
        for _ in range(self.threshold):
            for inputs,label in zip(training_inputs,labels):
                p=self.predict(inputs)
                self.weights[1:]+=self.learning_rate*(label-p)*inputs
                self.weights[0]+=self.learning_rate*(label-p)

model=Perceptron(3)
training_inputs=np.array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,1,1]])
labels=np.array([[0],[1],[1],[0],[1],[1]])

model.fit(training_inputs,labels)

test=np.array([1,0,1])
print(model.predict(test))
        
