import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

class Body():
    M = 0
    Q = 0
    Vs = [0, 0]
    Coords = [0, 0]

# Константы.
SECONDS_IN_DAY = 24 * 60 * 60
YEARS = 1
G = 6.67 * 10**(-11)
K = 8.98755 * 10**9

def move_func(bodys: list):
    N = len(bodys) # Количество тел.
    outList = []
    for i in range(N):
        m_i = bodys[i].M # Масса i-ого тела.
        q_i = bodys[i].Q # Заряд i-ого тела.
        x_i, y_i = bodys[i].Coords[0], bodys[i].Coords[1] # Координаты i-ого тела.
        
        dxdt_i, dydt_i = bodys[i].Vs[0], bodys[i].Vs[1]
        dv_xdt_i, dv_ydt_i = 0, 0
        
        for j in range(N):
            if i != j:
                m_j = bodys[j].M # Масса i-ого тела.
                q_j = bodys[j].Q # Заряд i-ого тела.
                x_j, y_j = bodys[j].Coords[0], bodys[j].Coords[1] # Координаты i-ого тела.
                
                dv_xdt_i += - (G * m_j * (x_i - x_j)) / ((x_i - x_j)**2 - (y_i - y_j)**2)**(1.5) + \
                         (K * q_i * q_j * (x_i - x_j)) / (((x_i - x_j)**2 - (y_i - y_j)**2)**(1.5) * m_i)
                
                dv_ydt_i += - (G * m_j * (y_i - y_j)) / ((x_i - x_j)**2 - (y_i - y_j)**2)**(1.5) + \
                         (K * q_i * q_j * (y_i - y_j)) / (((x_i - x_j)**2 - (y_i - y_j)**2)**(1.5) * m_i)       
        
        outList.append(dxdt_i)
        outList.append(dv_xdt_i)
        outList.append(dydt_i)
        outList.append(dv_ydt_i)
    
    return outList

# Создаём объект 1.
body_1 = Body()
# Задаём начальные параметры.
body_1.Coords = [149 * 10**9, 0]
body_1.Vs = [0, 30000]
body_1.M = 1.1 * 10**30
body_1.Q = - 1.1 * 10**20

# Создаём объект 2.
body_2 = Body()
# Задаём начальные параметры.
body_2.Coords = [- 149 * 10**9, 0]
body_2.Vs = [1, - 30000]
body_2.M = 2.1 * 10**30
body_2.Q = 2.1 * 10**20

# Создаём объект 3.
body_3 = Body()
# Задаём начальные параметры.
body_3.Coords = [0, 149 * 10**9]
body_3.Vs = [15000, 0]
body_3.M = 3.6 * 10**30
body_3.Q = - 3.1 * 10**20

# Решаем систему диф. ур.
t = np.arange(0, YEARS * 365 * SECONDS_IN_DAY, SECONDS_IN_DAY)
bodys = [body_1, body_2, body_3]
sol = odeint(move_func, bodys, t)

# Строим решение в виде графика и анимируем.
fig = plt.figure()
bodys = []

for i in range(len(t)):
    anim_body_1, = plt.plot(sol[:i, 0], sol[:i, 2], '-', color='r')
    anim_body_1_line, = plt.plot(sol[i, 0], sol[i, 2], '0', color='r')
    
    anim_body_2, = plt.plot(sol[:i, 4], sol[:i, 6], '-', color='g')
    anim_body_2_line, = plt.plot(sol[i, 4], sol[i, 6], '0', color='g')
    
    anim_body_3, = plt.plot(sol[:i, 8], sol[:i, 10], '-', color='b')
    anim_body_3_line, = plt.plot(sol[i, 8], sol[i, 10], '0', color='b')

anim = ArtistAnimation(fig, bodys)
plt.axis('equal')
anim.save('N_bodys_G+K.gif', writter='pillow', fps=60)