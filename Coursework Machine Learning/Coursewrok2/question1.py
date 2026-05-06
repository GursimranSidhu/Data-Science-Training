import numpy as np

def generate_dataset(theta, n, m):
    
    X = np.random.randn(n, m)
    
    ones = np.ones((n, 1))
    X = np.hstack((ones, X))
    
    beta = np.random.randn(m + 1, 1)
    
    z = np.dot(X, beta)
    prob = 1 / (1 + np.exp(-z))
    
    Y = (prob >= 0.5).astype(int)
    
    flip = np.random.rand(n, 1) < theta
    Y[flip] = 1 - Y[flip]
    
    return X, Y, beta


theta = 0.2
n = 10
m = 2

X, Y, beta = generate_dataset(theta, n, m)

print("X:\n", X)
print("\nY:\n", Y)
print("\nBeta used to generate Y:\n", beta)