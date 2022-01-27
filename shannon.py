import numpy as np

def sinc(t, k):
    return np.sin(np.pi*(t-k))/(np.pi*(t-k))

def shannon_interpolation(image, i, t):
    """Shannon-Whittaker interpolaton of the image on the row  i
    """
    n, m = image.shape
    X_tilde_it = 0
    for k_1 in range(0, m):
        if t != k_1 - m//2 :
            X_tilde_it += image[i][k_1]*sinc(t, k_1 - m//2)
    
    return X_tilde_it

def ground_truth_error(X_gd, X_h, t):
    """RMSE between X_gd (infinite signal) and X_h (finite signal)
    with X_h interpolated with a Shannon-Whittaker spline
    """
    res = 0
    n,m = X_gd.shape
    for i in range(n):
        res += ((shannon_interpolation(X_gd, i, t) - shannon_interpolation(X_h, i, t)))**2
    return res/n