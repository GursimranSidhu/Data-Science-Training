import numpy as np

def run_experiment(n, theta):
    
    m = 2
    
    X = np.random.randn(n, m)
    X = np.hstack((np.ones((n,1)), X))
    
    true_beta = np.random.randn(m+1,1)
    
    z = np.dot(X, true_beta)
    prob = 1 / (1 + np.exp(-z))
    Y = (prob >= 0.5).astype(int)
    
    flip = np.random.rand(n,1) < theta
    Y[flip] = 1 - Y[flip]

    beta = np.random.randn(m+1,1)
    
    for _ in range(500):
        h = 1/(1+np.exp(-np.dot(X,beta)))
        gradient = (1/n)*np.dot(X.T,(h-Y))
        beta -= 0.1*gradient
    
    print("n =", n, "theta =", theta)
    print("True Beta:", true_beta.flatten())
    print("Learned Beta:", beta.flatten())
    print("-"*40)


run_experiment(50, 0.0)
run_experiment(50, 0.3)
run_experiment(500, 0.0)
run_experiment(500, 0.3)