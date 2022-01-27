from scipy.interpolate import BSpline
from shannon import shannon_interpolation

def b_spline_interpolation(image, i, t):
    """bicubique interpolaton of the image on the row  i
    """
    n, m = image.shape
    X_tilde_it = 0
    spl = BSpline([i for i in range(m)], image[i][:], 3)
    return spl(t)

def ground_truth_error_spline(X_gd, X_h, t):
    """RMSE between X_gd (infinite signal) and X_h (finite signal)
    with X_h interpolated with a bicubique spline
    """
    res = 0
    n,m = X_gd.shape
    for i in range(n):
        res += ((shannon_interpolation(X_gd, i, t) - b_spline_interpolation(X_h, i, t)))**2
    return res/n