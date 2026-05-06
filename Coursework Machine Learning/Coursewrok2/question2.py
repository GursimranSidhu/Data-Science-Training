import numpy as np

def logistic_regression(X, Y, k, tau, learning_rate):
    
    n, m = X.shape
    
    beta = np.random.randn(m, 1)
    
    prev_cost = float('inf')
    
    for iteration in range(k):
        
        z = np.dot(X, beta)
        h = 1 / (1 + np.exp(-z))
        
        epsilon = 1e-10
        cost = -(1/n) * np.sum(Y*np.log(h+epsilon) + (1-Y)*np.log(1-h+epsilon))
        
        gradient = (1/n) * np.dot(X.T, (h - Y))
        
        beta = beta - learning_rate * gradient
        
        if abs(prev_cost - cost) < tau:
            break
        
        prev_cost = cost
    
    return beta, cost


X = np.array([[1, 0.5, 1.2],
              [1, -0.3, 0.8],
              [1, 1.5, -0.7],
              [1, -1.2, -0.4]])

Y = np.array([[1],
              [0],
              [1],
              [0]])

# ----- Sample Run -----
beta, final_cost = logistic_regression(X, Y, k=1000, tau=1e-6, learning_rate=0.1)

print("Learned Beta:\n", beta)
print("Final Cost:", final_cost)