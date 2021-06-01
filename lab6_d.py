import math
import matplotlib.pyplot as plt

# функция по варианту
def f(x, p):
    return math.atan(x) + p * (2 * x + 1)

# начальные данные по варианту
c = 0 # от
d = 2 # до
n = 30 # кол-во итераций
h = (d - c) / n # шаг

# отрезок локализации
a = -1.5
b = 1.5

eps = 0.001 # точность

print("   i ", "  left  ", " right", "  P  ", " middle  ")
# здесь по сути решается уравнение для n различных функций
for i in range(n + 1):
    # параметр
    p = c + i * h
    
    # отрезок локализации
    left = a
    right = b
    
    # середина отрезка локализации
    middle = (right + left) / 2
    # длина отрезка л.
    length = right - left
    
    # из этого используется только знак произведения (см. алгоритм)
    ff = f(left, p) * f(middle, p)
    
    while(length > eps):
        # см. алгоритм
        left = left if (ff < 0) else middle
        right = middle if (ff < 0) else right
        middle = (right + left) / 2
        
        length = right - left
        ff = f(left, p) * f(middle, p)
        
    # вывели решение данного уравнения (одного из n)
    print(str(i + 1).rjust(4), " | ", "%.4f" % left, "  ", "%.4f" % right, "  ", "%.4f" % p, "  ", "%.6f" % middle, sep = "")

# график 
#
# список иксов для построения графика
x0 = [x * 0.1 for x in range(-10,10 + 2,2)]
y1 = list()

# функция при p = c
for x in x0:
    y1.append(f(x, c))

# p = d
y2 = list()
for x in x0:
    y2.append(f(x, d))
    
# бахаем график
# для более корретного масштаба - комментить одно из двух
plt.plot(x0, y1, label="F(x, c)")
plt.plot(x0, y2, label="F(x, d)")
plt.legend(loc="best")
plt.show()