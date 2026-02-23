import numpy as np
def getBondPrice(y, face, couponRate, m, ppy=1):
    r = y / ppy
    n = m * ppy
    cf = face * couponRate / ppy
    t = np.arange(1, n + 1, 1)
    x = np.sum(cf/(1+r)**t) + face / (1+r)**n
    return(x)
