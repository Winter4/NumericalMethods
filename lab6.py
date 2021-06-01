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

# отрезок локализации
a = -1.5
b = 1.5

eps = 0.001 # точность

print("   i ", "  left  ", " right", "  P  ", " middle  ")
for i in range(n + 1):
    p = c + i * h
    
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
        
    print(str(i + 1).rjust(4), " | ", "%.4f" % left, "  ", "%.4f" % right, "  ", "%.1f" % p, "  ", "%.6f" % middle, sep = "")

x0 = [x * 0.1 for x in range(-10,10,2)]
y1 = list()
for x in x0:
    y1.append(f(x, c))
    
y2 = list()
for x in x0:
    y2.append(f(x, d))
    
plt.plot(x0, y1, label="F(x, c)")
plt.plot(x0, y2, label="F(x, d)")
plt.legend(loc="best")
plt.show()