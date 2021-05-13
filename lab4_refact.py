import math

def function(x_required):
    return math.exp(math.sin(x_required))

def d1_manual(x_required):
    return math.exp(math.sin(x_required) * math.cos(x_required))

def d2_manual(x_required):
    return (-math.sin(x) + (math.cos(x_required))**2) * math.exp(math.sin(x_required))
    
def d1_nuton(x_required, step, x_source, y_source, diffs):
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

def d2_nuton(x_required, step, x_source, y_source, diffs):
    q = (x_required - x_source[0]) / step
    
    result = diffs[2][0] # Будущий результат
    factorial = 2 # Накопление факториала
    
    for i in range(3, len(diffs)): # Самый внешний цикл (сумма)  1
        bracket_sum = 0 # Накопление 
        factorial *= i
        
        for j in range(i): # Сумма по j                          2
            
            for k in range(i): # Сумма по k                      3        
                if (k != j):   #                                 4
                    bracket_product = 1.0
                    for l in range(i): # Произведение по l       5
                        if (l != k and l != j): #                6
                            bracket_product *= q - l
                    bracket_sum += bracket_product
            
        result += bracket_sum * diffs[i][0] / factorial
    return result / step**2

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
    
# __________________________________ main ______________________________________
    
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

for x in args:
    print("%6.2f" % x, "%11.6f" % d1_nuton(x, step, x_source, y_source, diffs), "%11.6f" % d1_manual(x), "%11.6f" % d2_nuton(x, step, x_source, y_source, diffs), "%11.6f" % d2_manual(x))