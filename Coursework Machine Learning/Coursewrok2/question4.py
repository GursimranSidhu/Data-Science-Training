import numpy as np

def logistic_reg_regularized(X, Y, reg_type, reg_lambda):
    
    n, m = X.shape
    beta = np.random.randn(m,1)
    
    for _ in range(1000):
        
        h = 1/(1+np.exp(-np.dot(X,beta)))
        gradient = (1/n)*np.dot(X.T,(h-Y))
        
        if reg_type == "L2":
            gradient += (reg_lambda/n)*beta
        
        if reg_type == "L1":
            gradient += (reg_lambda/n)*np.sign(beta)
        
        beta -= 0.1*gradient
    
    return beta


X = np.array([[1, 0.2, 0.5],
              [1, -1.2, 0.7],
              [1, 1.5, -0.8],
              [1, -0.3, -1.1]])

Y = np.array([[1],
              [0],
              [1],
              [0]])

print("L2 Regularization Beta:")
print(logistic_reg_regularized(X, Y, "L2", 0.5))

print("\nL1 Regularization Beta:")
print(logistic_reg_regularized(X, Y, "L1", 0.5))