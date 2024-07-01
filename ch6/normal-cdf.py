import math
import matplotlib.pyplot as plt

xs = [x / 10.0 for x in range(-50,50)]

def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1+math.erf((x-mu)/math.sqrt(2)/sigma)) / 2

plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
plt.plot(xs,[normal_cdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=1')
plt.plot(xs,[normal_cdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=1')
plt.plot(xs,[normal_cdf(x,mu=-1) for x in xs],'-.',label='mu=0,sigma=1')
plt.legend(loc=4)
plt.show()

def binary_search(p: float,
                  mu: float = 0,
                  sigma: float = 1,
                  tolerance: float = 0.00001) -> float:
    if mu != 0 or sigma != 1:
        return mu+sigma*binary_search(p,tolerance=tolerance)
    low_z=-10.0
    high_z=10.0
    while high_z - low_z > tolerance:
        mid_z = (low_z + high_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z = mid_z
        else:
            high_z = mid_z
    return mid_z
