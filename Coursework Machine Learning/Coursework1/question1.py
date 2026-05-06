import numpy as np
def generate_dataset(sigma, n ,m):
    X=np.random.randn(n,m)
    X[: ,0]=1
    beta=np.random.randn(m,1)
    e=np.random.normal(0,sigma,(n,1))
    y=np.dot(X,beta)+e
    return X,y, beta


X, y, beta = generate_dataset(1, 5, 3)

print("X = ")
print(X)

print("y = ")
print(y)

print("beta = ")
print(beta)
