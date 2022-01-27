import numpy as np

def phi(X):
    n, m = X.shape
    DFT_X = None
    for i in range(n):
        X_i = np.array([X[i][k] for k in range(m)])
        fft = np.fft.fft(X_i)
        n_fft = len(fft)
        fft_real = np.array([0. for i in range(n_fft)])
        
        if DFT_X is None:
            DFT_X = np.array([0. for i in range(n_fft)])
        for i in range(n_fft):
          a = np.abs(fft[i])**2
          fft_real[i] = a.real
        DFT_X += fft_real
    return 1/n*DFT_X

def sigma_prime_cal(phi_l, alpha):
    n = len(phi_l)
    timestep = 0.1
    freq = np.fft.fftfreq(n, d=timestep)
    freq = np.fft.fftshift(freq)
    maxi = 0
    for i in range(n):
        if freq[i] >= alpha*np.pi and phi_l[i] >= maxi:
            maxi = phi_l[i]
    return phi_l[i]

def sigma_cal(phi_l, sigma_prime):
    res = 0
    timestep = 0.1
    n = len(phi_l)
    freq = np.fft.fftfreq(n, d=timestep)
    freq = np.fft.fftshift(freq)
    for i in range(n):
        res += 2/(1 + np.cos(freq[i]))*max(0, phi_l[i] - sigma_prime**2)
    return np.sqrt(res/n)