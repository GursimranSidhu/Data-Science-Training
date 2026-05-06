"""The purpose of this investigation is to analyze how:

n (dataset size)

sigma (noise level)

affect the ability of a Linear Regression model using Gradient Descent to correctly learn the true coefficients β used to generate the dataset.

The data is generated using
y=Xβ+e

where X is the design matrix, β is the vector of true coefficients, and e is the noise term drawn from a normal distribution with mean 0 and standard deviation sigma."""

import numpy as np
def generate_dataset(sigma, n ,m):
    X=np.random.randn(n,m)
    X[: ,0]=1
    beta=np.random.randn(m,1)
    e=np.random.normal(0,sigma,(n,1))
    y=np.dot(X,beta)+e
    return X,y, beta

def gradient_descent(X , y, k, tau, lr):
    n, m = X.shape
    beta = np.zeros((m, 1))
    prev_cost=float("inf")
    for i in range(k):
        y_pred = np.dot(X, beta)
        error = y_pred - y
        cost = (1/2*n) * np.sum(error**2)
        if abs(prev_cost - cost) < tau:
            break
        prev_cost = cost
        gradient = (1/n) * np.dot(X.T, error)
        beta -= lr * gradient
    return beta, cost

if __name__ == "__main__":
    sigma_values = [0.1, 1, 10]
    n_values = [100, 1000, 10000]
    m = 5
    k = 1000
    tau = 0.0001
    lr = 0.01

    for sigma in sigma_values:
        for n in n_values:
            X, y, true_beta = generate_dataset(sigma, n, m)
            estimated_beta, final_cost = gradient_descent(X, y, k, tau, lr)
            print(f"Sigma: {sigma}, n: {n}")
            print("Estimated beta:")
            print(estimated_beta.flatten())
            print("True beta:")
            print(true_beta.flatten())
            print("Final cost:")
            print(final_cost)
            print("-" * 50)