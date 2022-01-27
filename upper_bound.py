import numpy as np
from scipy import interpolate
from shannon import sinc

def upper_bound(t, mu, K, sigma, sigma_prime):
    upper_bound = 0
    if t != 0:
        delta = min(K+1/2 - t, K+1/2+t)
        Delta = max(K+1/2 - t, K+1/2+t)
        if delta + 1/2 == 0 or delta == 0:
            delta = 1
        if Delta == 0 or Delta + 1/2 == 0:
            Delta = 1
        upper_bound = (np.sin(np.pi*t)/np.pi)**2*((mu**2 + 4*sigma**2)*(1/(delta + 1/2) + 1/(Delta+1/2))**2 + 2*sigma_prime**2*(1/delta + 1/Delta))
    return upper_bound



def enveloppe_cal(curve, t):
    time = [t[0]]
    pics = [curve[0]]
    n = len(curve)
    for i in range(n-2):
        if curve[i] - curve[i+1] <=0 and curve[i+1] - curve[i+2] >=0:
          pics.append(curve[i+1])
          time.append(t[i+1])
    time.append(t[-1])
    pics.append(curve[-1])
    f = interpolate.interp1d(time, pics)
    res = []
    for i in t:
        res.append(f(i))
    return np.array(res)