import math

def function(x_required):
    return math.exp(math.sin(x_required))

def d1(x_required):
    return math.exp(math.sin(x_required) * math.cos(x_required))

def d2(x_required):
    return (-math.sin(x) + (math.cos(x_required))**2) * math.exp(math.sin(x_required))

def print_diffs(diffs):
    # шапка таблицы разностей
    for i in range(len(diffs)):
        print(" dY[", i + 1, "]     ", sep = "", end = "")
    print()
    
    # значения таблицы разностей
    for i in range(len(diffs)):
        for j in range(len(diffs[i])):
            print("%-11.6f" % diffs[j][i], sep = "", end = "")
        print()
    print()
    
def differentiate_first(x_required, step, x_source, y_source, diffs):
    q = (x_required - x_source[0]) / step 
    
    result = 0.0 # Будущий результат
    factorial = 1 # Накопление факториала
    
    for i in range(len(diffs)): # Самый внешний цикл (сумма)
        bracket_sum = 0.0 # Накопление суммы
        
        for j in range(i): # Сумма произведений (Сумма по j)
            bracket_product = 1 # Накопление произведения
            for k in range(i): # Произведения разности q - k (Произведение по k)
                if (k != j): bracket_product *= q - k
            bracket_sum += bracket_product # Собственно накопление
                       
        factorial *= i + 1 # Вычисление факториала
        
        # Проверяем на умножение на 0
        result += diffs[i][0] / factorial if (bracket_sum == 0) else diffs[i][0] / factorial * bracket_sum
        #print("Bracket sum", i, bracket_sum) # Отладочный принт
        
    return result / step

def differentiate_second(x_required, step, x_source, y_source, diffs):
    q = (x_required - x_source[0]) / step
    
    result = 0.0 # Будущий результат
    factorial = 1 # Накопление факториала
    
    for i in range(2, len(diffs)): # Самый внешний цикл (сумма)
        bracket_sum1 = 0 # Накопление 
        
        for j in range(i): # Сумма по j
            bracket_sum2 = 0.0
            
            for k in range(i): # Сумма по k
                bracket_product = 1.0
                if (k != j):
                    for l in range(i): # Произведение по l
                        if (l != k and l != j): bracket_product *= q - l
                    bracket_sum2 += bracket_product
            
            bracket_sum1 += bracket_sum2
        result += diffs[i][0] / factorial * bracket_sum1
    return -result / step**2

def differentiate_first_manual(x_required, step, x_min, diffs):
    t = (x_required - x_min) / step
    
    tmp = []
    tmp.append(diffs[0][0])
    tmp.append((2*t - 1) / 2 * diffs[1][0])
    tmp.append((3*t**2 - 6*t**2 + 2) / 6 * diffs[2][0])
    tmp.append((4*t**3 - 18*t**2 + 22*t - 6) / 24 * diffs[3][0])
    #tmp.append(())
    return sum(tmp) / step

def differentiate_second_manual(x_required, step, x_min, diffs):
    t = (x_required - x_min) / step
    
    tmp = []
    tmp.append(diffs[1][0])
    tmp.append((t - 1)*diffs[2][0])
    tmp.append((6*t**2 - 18*t + 11) / 12 * diffs[3][0])
    
    return -sum(tmp) / step**2
    
    # main
    
x_source = [] # список аргументов
y_source = [] # список значений функции

x_right = 1.0   # правая граница
x_left = 0.0    # левая граница
values_number = 10 + 1 # количество узлов
step = (x_right - x_left) / values_number # интервал между узлами

# конечные разности
diffs = []

# для большей точности - шаг 1.1
step += step / values_number

x_source.append(x_left) # первое значение X
y_source.append(function(x_source[0])) # первое значение Y 

# заполнение таблицы значений функции
for i in range(1, values_number):
    x_source.append(x_source[i - 1] + step) # X
    y_source.append(function(x_source[i]))  # Y

# генерация таблицы разностей
#
# заполнение первого столбца
diffs.append([0.0] * (values_number - 1)) 
for i in range(len(diffs[0])):
    diffs[0][i] = y_source[i + 1] - y_source[i]

# заполнение остальных столбцов
for diff_len in range(values_number - 2, 0, -1):
    # создание списка (разности k порядка)
    diffs.append([0.0] * diff_len)

    # текущий индекс с начала списка
    column_index = values_number - 1 - diff_len
    
    # для всех разностей этого порядка
    for i in range(diff_len):
        # заполнение разностей
        diffs[column_index][i] = diffs[column_index - 1][i + 1] - diffs[column_index - 1][i]
            
print_diffs(diffs)

print("  X", "d1 N", "d1 M", "d2 N", "d2 M", sep = 8 * " ")
args = [-0.18, 0.18, -0.45, 0.45, 0.775, 1.225, 0.55, 1.45]
#print (differentiate_first(0.18, step, x_source, y_source, diffs))
#print (differentiate_second(0.18, step, x_source, y_source, diffs))
#print()
#print(differentiate_first_manual(0.18, step, x_source[0], diffs))
#print(differentiate_second_manual(0.18, step, x_source[0], diffs))

for x in args:
    #print("%6.2f" % x, "%11.6f" % differentiate_first(x, step, x_source, y_source, diffs), "%11.6f" % differentiate_second(x, step, x_source, y_source, diffs), "%11.6f" % differentiate_first_manual(x, step, x_source[0], diffs), "%11.6f" % differentiate_second_manual(x, step, x_source[0], diffs))

    print("%6.2f" % x, "%11.6f" % differentiate_first(x, step, x_source, y_source, diffs), "%11.6f" % d1(x), "%11.6f" % differentiate_second(x, step, x_source, y_source, diffs), "%11.6f" % d2(x))