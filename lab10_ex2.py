import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определяем переменную величину
t = np.arange(-1, 1, 0.01)

# Определяем функцию для системы диф. уравнений
def diff_func(tmp, t): # z - изменяемая величина для системы
    x, y = tmp # Указание изменяемых функций, через z
	
    # Первое уравнение системы
    dx_dt =3 * x - 2 * y + np.exp(3*t) / (np.exp(t) + 1)
    # Второе уравнение системы
    dy_dt = x - np.exp(3 * t) / (np.exp(t) + 1)
    
    return dx_dt, dy_dt

# Определяем начальные значения и параметры,
# входящие в систему диф. уравнений
y0 = -7
x0 = 5

# Начальное значение изменяемой величины системы
tmp0 =x0, y0


# Решаем систему диф. уравнений
sol = odeint(diff_func, tmp0, t)

# Строим решение в виде графика
plt.plot(t, sol[:, 1], 'b', label='y(x)')

plt.legend()
plt.show()