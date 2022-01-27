import numpy as np

def add_noise(n,m, sigma):
    noisy_image = np.zeros((n,m))
    
    mini = np.inf
    for i in range(n):
        for j in range(m):
            noisy_image[i][j] += np.random.normal(0,sigma)
            if noisy_image[i][j] < mini:
                mini = noisy_image[i][j]
        
    return noisy_image