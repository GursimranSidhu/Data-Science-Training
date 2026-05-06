import numpy as np

class LogisticRegression:
    
    def __init__(self, learning_rate=0.1, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.beta = None
    
    def fit(self, X, Y):
        n, m = X.shape
        self.beta = np.random.randn(m,1)
        
        for _ in range(self.epochs):
            h = 1/(1+np.exp(-np.dot(X,self.beta)))
            gradient = (1/n)*np.dot(X.T,(h-Y))
            self.beta -= self.learning_rate*gradient
    
    def predict(self, X):
        h = 1/(1+np.exp(-np.dot(X,self.beta)))
        return (h>=0.5).astype(int)


X = np.array([[1, 0.5, 1.2],
              [1, -0.3, 0.8],
              [1, 1.5, -0.7],
              [1, -1.2, -0.4]])

Y = np.array([[1],
              [0],
              [1],
              [0]])

model = LogisticRegression()
model.fit(X, Y)

print("Learned Beta:\n", model.beta)
print("Predictions:\n", model.predict(X))