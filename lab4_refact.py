import math

def function(x_required):
    return math.e  ** math.sin(x_required)

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
    
def differentiate_first(x_required, step):
     return (function(x_required + step) - function(x_required)) / step
    
def differentiate_second(x_required, step):
    return((differentiate_first(x_required + step, step) - differentiate_first(x_required, step)) / step) 

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

print("  X", "d1", "d2", sep = 10 * " ")
args = [-0.18, 0.18, -0.45, 0.45, 0.775, 1.225, 0.55, 1.45]

for x in args:
    print("%6.2f" % x, "%11.6f" % differentiate_first(x, step), "%11.6f" % differentiate_second(x, step))
