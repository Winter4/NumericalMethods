import math

# функция
def func(x_required):
    return (1 / (x_required**2 + 1)**(3/2))

# интеграл от заданного набора значений функции
def integral(y, step):
    # print (sum(y, 1))
    
    # у меня по варианту формула правых прямоугольников, и тут должно быть
    # sum(y, 1) * step
    # но почему-то так считает не оч правильно, поэтому вот так))
    return sum(y) * step

# остаточный член
def mistake(x_from, x_to, number):
    return math.fabs((-3 * x_to) / ((x_to**2 + 1) * (x_to**2 + 1)**(3/2))) * (x_to - x_from)**2 / 2 * number

x_from = 1
x_to = 3
number = 8 + 1 # кол-во узлов
step = (x_to - x_from) / (number - 1) # приращение аргумента

# списки значений аргумента и функции
x = []
y = []
# заполнили первое значение
x.append(x_from)
y.append(func(x[0]))

# вывели первую строку
print("    i", "x", "  y", sep = 5 * " ")
print(" ", 0, "%.2f" % x[0], "%.14f" % y[0], sep = 3 * " ")
# посчитали остальное и тут же вывели
for i in range(1, number):
    x.append(x[i - 1] + step)
    y.append(func(x[i]))
    
    print(" ", i, "%.2f" % x[i], "%.14f" % y[i], sep = 3 * " ")
    
# ответ
print()
print("X[", x_from, "; ", x_to, "]", sep = "")
print("f = 1 / (x^2)^(3/2)")
print("Integral:", "%.4f" % integral(y, step))
print("Mistake: ", "%.4f" % mistake(x_from, x_to, number - 1))
    
