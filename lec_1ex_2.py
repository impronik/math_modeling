import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

class Body():
    Coord_x, Coord_y = 0, 0
    V_x, V_y = 0, 0
    M = 0
    Q = 0
    
    def debug(self):
        print('------------------------------------------',
              f'Coord X|Y : {self.Coord_x}|{self.Coord_y}',
              f'V X|Y : {self.V_x}|{self.V_y}',
              f'M : {self.M}',
              f'Q : {self.Q}', sep='\n')

# Константы.
SECONDS_IN_DAY = 24 * 60 * 60
YEARS = 1
G = 6.67 * 10**(-11)
K = 8.98755 * 10**9

def dvdt(body_1, body_2, axis):
    dx = body_1.Coord_x - body_2.Coord_x
    dy = body_1.Coord_y - body_2.Coord_y
    if axis == 'x':
        dv_xdt = - (G * body_2.M * (dx)) / ((dx)**2 + (dy)**2)**(1.5) + \
                 (K * body_1.Q * body_2.Q / body_1.M * (dx)) / ((dx)**2 + (dy)**2)**(1.5)
        
        return dv_xdt
    elif axis == 'y':
        dv_ydt = - (G * body_2.M * (dy)) / ((dx)**2 + (dy)**2)**(1.5) + \
                 (K * body_1.Q * body_2.Q / body_1.M * (dy)) / ((dx)**2 + (dy)**2)**(1.5)
                 
        return dv_ydt

def move_func(y0, t):
    bodys = []
    for i in range(0, len(y0), 4):
        body_i = Body() # Создаём i-ое тело.
        
        # Задаём начальные параметры i-ого тела
        body_i.Coord_x, body_i.Coord_y = y0[i], y0[i + 1]
        body_i.V_x, body_i.V_y = y0[i + 2], y0[i + 3]
        body_i.M = m[i % 4]
        body_i.Q = q[i % 4]
        
        bodys.append(body_i) # Добавляем тело в список.
        
        print(y0)
        #body_i.debug()
     
    y = []
    N = len(bodys) # Количество тел в системе.
    for i in range(N):
        dxdt_i, dydt_i = bodys[i].V_x, bodys[i].V_y
        dv_xdt_i, dv_ydt_i = 0, 0
        for j in range(N):
            if i != j:
                dv_xdt_i += dvdt(bodys[i], bodys[j], 'x')
                dv_ydt_i += dvdt(bodys[i], bodys[j], 'y')
                      
        y.append(dxdt_i)
        y.append(dydt_i)
        y.append(dv_xdt_i)
        y.append(dv_ydt_i)
    
    return y


# Задаём начальные параметры.
x_1 = 149 * 10**9
y_1 = 0
v_x_1 = 0
v_y_1 = 30000
m_1 = 1.1 * 10**30
q_1 = - 1.1 * 10**20

x_2 = - 149 * 10**9
y_2 = 0
v_x_2 = 1
v_y_2 = - 30000
m_2 = 2.1 * 10**30
q_2 = 2.1 * 10**20

x_3 = 0
y_3 = 149 * 10**9
v_x_3 = 15000
v_y_3 = 0
m_3 = 3.6 * 10**30
q_3 = - 3.1 * 10**20

# Решаем систему диф. ур.
m = [m_1, m_2, m_3]
q = [q_1, q_2, q_3]
y0 = [x_1, y_1, v_x_1, v_y_1,
      x_2, y_2, v_x_2, v_y_2,
      x_3, y_3, v_x_3, v_y_3]
t = np.arange(0, YEARS * 365 * SECONDS_IN_DAY, SECONDS_IN_DAY)
sol = odeint(move_func, y0, t)

# Строим решение в виде графика и анимируем.
fig = plt.figure()
bodys = []

for i in range(len(t)):
    anim_body_1, = plt.plot(sol[:i, 0], sol[:i, 2], '-', color='r')
    anim_body_1_line, = plt.plot(sol[i, 0], sol[i, 2], 'o', color='r')
    
    anim_body_2, = plt.plot(sol[:i, 4], sol[:i, 6], '-', color='g')
    anim_body_2_line, = plt.plot(sol[i, 4], sol[i, 6], 'o', color='g')
    
    anim_body_3, = plt.plot(sol[:i, 8], sol[:i, 10], '-', color='b')
    anim_body_3_line, = plt.plot(sol[i, 8], sol[i, 10], 'o', color='b')
    
    bodys.append([anim_body_1, anim_body_1_line,
                  anim_body_2, anim_body_2_line,
                  anim_body_3, anim_body_3_line])

anim = ArtistAnimation(fig, bodys)
plt.axis('equal')
anim.save('N_bodys_G+K.gif', writer='pillow', fps=60)