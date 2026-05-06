import numpy as np
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

n=5
m=3
X= np.random.randn(n, m)
X[:,0]=1

true_beta = np.random.randn(m, 1)
y=X.dot(true_beta) + np.random.normal(0, 1, (n, 1))
beta, final_cost = gradient_descent(
    X,
    y,
    k=1000,      
    tau=0.0001,  
    lr=0.01      
)
print("Estimated beta:")
print(beta)
print("True beta:")
print(true_beta)
print("Final cost:")
print(final_cost)