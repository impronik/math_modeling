import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def F(m, t):
    dmdt  = m*k*t
    return dmdt

t = np.linspace(0, 10, 100)
m_0 = 1000
k = -0.08


solve_Bi =odeint(F, m_0, t)


plt.plot(t, solve_Bi[:,0] )
plt.show()