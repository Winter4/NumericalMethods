import math

def function(x_required):
    return math.e  ** math.sin(x_required)

def interpolate(x_required, x_left, x_right, diffs, step):
    # первый полином
    if (math.fabs(x_required - x_left) < math.fabs(x_required - x_right)):
        result = y[0]

        # итерация цикла - одно слагаемое полинома
        for k in range(1, values_number):
            a = diffs[k - 1][0] / math.factorial(k) / step**k

            for i in range(k):
                a *= x_required - x[i]

            result += a

    # второй полином
    else:
        result = y[values_number - 1]

        # итерация цикла - одно слагаемое полинома
        for k in range(values_number - 2, 0, - 1):
            now_index = values_number - 1 - k

            a = diffs[now_index - 1][k] / math.factorial(now_index) / step**now_index

            for i in range(values_number - 1, k, -1):
                a *= x_required - x[values_number - 1]

            result += a

    return result

def print_diffs():
    for i in range(len(self.diffs)):
        print("dY[", i + 1, "]      ", sep = "", end = "")
    print()

    for i in range(len(self.diffs)):
        for j in range(len(self.diffs[i])):
            print("%-11.6f" % self.diffs[j][i], sep = "", end = "")
        print()
    print()

    # main
    
x_source = [] # список аргументов
y_source = [] # список значений функции

x_right = 1.0   # правая граница
x_left = 0.0    # левая граница
values_number = 10 + 1 # количество узлов
step = (x_right - x_left) / values_number # интервал между узлами

diffs = []

# для большей точности - шаг 1.1
step += step / values_number

x.append(x_left) # первое значение X
y.append(function(x[0])) # первое значение Y 

# заполнение функции
for i in range(1, values_number):
    x.append(x[i - 1] + step) # X
    y.append(function(x[i]))  # Y

# генерация таблицы разностей
#
# заполнение первого листа
diffs.append([0.0] * (values_number - 1)) 
for i in range(values_number - 1):
    diffs[0][i] = y[i + 1] - y[i]

# заполнение остальных листов
for diff_len in range(values_number - 2, 0, -1):
    # создание списка (разности k порядка)
    diffs.append([0.0] * diff_len)

    # для всех разностей этого порядка
    for i in range(diff_len):
        now_index = valuesNumber - 1 - diff_len

        # заполнение разностей
        diffs[now_index][i] = diffs[now_index - 1][i + 1] - diffs[now_index - 1][i]

        # вывод разностей
        #print("%.5f" % self.diffs[self.valuesNumber - 1 - diffLen][i], end = " ")
    #print()


        

            
one = Lab()
one.printDiffs()
#arg = float(input(" Enter argument: "))
#print(math.e**math.sin(arg))
#print(one.interpolate(arg))

print("X", "Ftrue", "FN", "mis", sep = "       ")
args = [-0.18, 0.18, -0.45, 0.45, 0.775, 1.225, 0.55, 1.45]
