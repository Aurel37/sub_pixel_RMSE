import numpy as np

def kron(image, lbda):
    """kron operation to get
    a poorly sampled image
    """
    n, m = image.shape
    resize = np.zeros((n//lbda, m//lbda))
    # take a pixel every lbda
    for i in range(n//lbda):
        for j in range(m//lbda):
            resize[i][j] = image[i*lbda][j*lbda]
    # kron operator
    res = np.kron(resize, np.ones((lbda, lbda)))
    return res[0:n, 0:m]