import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def F(v, t):
    dvdt  = k*v**2 / m + a_0 
    return dvdt

t = np.linspace(0, 25, 100)
k = - 0.37
v_0 = 0
m = 20
a_0 = 5

solve_Bi =odeint(F, v_0, t)


plt.plot(t, solve_Bi[:,0] )
plt.show()