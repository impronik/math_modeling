import numpy as np
import matplotlib.pyplot  as plt
from matplotlib.animation import FuncAnimation

try:
    k = float(input('Введите коэффицент сопротивления (0; 1) = '))
    if  not(0 < k < 1):
        k = 0.35
        print('Ошибка неверное значение коэффицента сопротивления (k = 0.35) ')
except:
    k = 0.35
    print('Ошибка неверное значение коэффицента сопротивления (k = 0.35) ')
try:
    V_0 = float(input('Введите начальную скорость (0; +oo) = '))
    if V_0 < 0:
        V_0 = 60
        print('Ошибка неверное значение скорости (V_0 = 60)')
except:
    V_0 = 60
    print('Ошибка неверное значение скорости (V_0 = 60)')
try:
    m = float(input('Введите массу объекта (0;+oo) = '))
except:
    m = 2500
    print('Ошибка неверное значение массы (m = 2500)')
g = 9.8

F_tr = (k *m*g)
T = V_0/(k*g)
S = (m*V_0**2)/(2*F_tr)

fig, ax = plt.subplots()

ax.set_xlim(0, S + S/10)
ax.set_ylim(-1, 1)


obj_road = plt.plot([0, 2*S], [-0.1 ,-0.1], lw = 3, color = 'k' )

obj_line, = plt.plot([], [],'--' ,lw = 1, color = 'k')
obj_body, = plt.plot([],[],'>' ,ms = 20, color = 'b')



Xline = []

def update(t):
    x = V_0*t - (F_tr*t**2)/(2*m)
    Xline.append(x)
    
    obj_line.set_data(Xline,0)
    obj_body.set_data(Xline[::-1][0],0)
    
    ax.set_xlabel(f'Путь: {np.around(x, 3)} метров')
    ax.set_title(f'Время:{np.around (t, 3)} секунд')
    
    
print(f'Время на торомжение тела: {np.around(T, 3)} секунд')
print(f'Тормозной путь: {np.around(S, 3)} метров')    

t = np.linspace(0, T, 100)
anim = FuncAnimation(fig, update, t )
anim.save('Breaking_distances.gif', writer = 'pillow', fps = 30)
