import math
import matplotlib.pyplot as plt

# функция по варианту
def f(x, p):
    return math.sin(2 * x) - p * x**2

# начальные данные по варианту
c = 1 # от
d = 10 # до
n = 30 # кол-во итераций
h = (d - c) / n # шаг

eps = 0.001 # точность

print("   i ", "  from  ", "  to   ", "  P  ", " middle  ")
for i in range(n + 1):
    p = c + i * h
    
    # отрезок локализации
    x = 0.1
    step = 0.1
    while (f(x, p) * f(x + step, p) > 0):
        x += step
    a = x
    b = x + step
    
    left = a
    right = b
    
    middle = (right + left) / 2
    length = right - left
    
    ff = f(left, p) * f(middle, p)
    
    while(length > eps):
        left = left if (ff < 0) else middle
        right = middle if (ff < 0) else right
        middle = (right + left) / 2
        
        length = right - left
        ff = f(left, p) * f(middle, p)
        
    print(str(i + 1).rjust(4), " | ", "%.4f" % a, "  ", "%.4f" % b, "  ", "%.1f" % p, "  ", "%.6f" % middle, sep = "")

x0 = [x * 0.01 for x in range(-30, 100, 1)]
y1 = list()
for x in x0:
    y1.append(f(x, c))
    
y2 = list()
for x in x0:
    y2.append(f(x, d))

plt.plot(x0, y1, label="F(x, c)")
plt.plot(x0, y2, label="F(x, d)")
plt.legend(loc="best")
plt.axhline(0, linewidth=0.8, color="black")
plt.axvline(0, linewidth=0.8, color="black")
plt.show()