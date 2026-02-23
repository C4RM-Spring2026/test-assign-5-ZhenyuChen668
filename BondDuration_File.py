import numpy as np
def getBondDuration(y, face, couponRate, m, ppy = 1):
    r = y/ppy
    n = m * ppy
    cf = face * couponRate / ppy
    t = np.arange(1, n + 1, 1)
    a = np.sum(cf/(1+r)**t) + face / (1+r)**n
    b = np.sum(cf * t /(1+r)**t) + face * n / (1+r)**n
    x = b/a/ppy
    return(x)
