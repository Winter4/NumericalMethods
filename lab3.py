import math 

def function(xRequired):
    return math.sin(math.exp(xRequired))

def printLists(message, xPrint, yPrint):
    print()
    print(message)
    print(" X |", end = "")
    for i in range(len(xPrint)):
        print("%8.5f" % (xPrint[i]), end = "")
    print()

    print(" Y |", end = "")
    for i in range(len(yPrint)):
        print("%8.5f" % (yPrint[i]), end = "")
    print()
    
def interpolate(xRequired, xUsed, yUsed):
    xEitkin = [] # матрица значений иксов
    size = len(xUsed) # размер матрицы значений иксов
    dEitkin = [1.0] * size  # произведение иксов в строке
    ydEitkin = [1.0] * size # Yi/Di
    
    mainProduct = 1 # произведение иксов на главной диагонали
    ydSum = 0 # сумма Yi/Di
    
    print("\n  Eitkin table: ")
    # заполнение матрицы иксов
    for i in range(size):
        
        xEitkin.append([0.0] * size) # создали список из size элементов
        for j in range(size):
            # вычисление икса
            if (j == i): # если на главной диагонали
                xEitkin[i][j] = xRequired - xUsed[i] 
                mainProduct *= xEitkin[i][j]
            else: xEitkin[i][j] = xUsed[i] - xUsed[j]
            print(" %8.5f" % xEitkin[i][j], end = " ") # вывели икс
            
            dEitkin[i] *= xEitkin[i][j] # домножили икс
            
        ydEitkin[i] = yUsed[i] / dEitkin[i] # посчитали Yi/Di
        ydSum += ydEitkin[i] # добавили к сумме
        print(" ||", "%8.5f" % dEitkin[i], "%8.5f" % yUsed[i], "%14.5f" % ydEitkin[i], sep = " ") # вывели столбцы после иксов
    
    print("\n Main product: ", "%.5f" % mainProduct, sep = "")
    print(" Y/D sum: ", "%.5f" % ydSum)
    return mainProduct * ydSum

# _________________________________________________________    
    
xSource = [] # список значений аргумента
ySource = [] # список значений функции

xLeft = 0 # левая граница значений аргумента
xRight = 0.2 # правая граница значений аргумента
nodesNumber = 11 # количество узлов интерполирования
step = (xRight - xLeft) / nodesNumber # шаг икса

# __________ таблица значений функции _______
#
xSource.append(xLeft) # первое значение X
ySource.append(function(xLeft)) # -||-  Y
for i in range(1, nodesNumber  + 1):
    xSource.append(xSource[i - 1] + step) # заполнение X
    ySource.append(function(xSource[i]))  # заполнение Y
# ___________________________________________

# вывод полной таблицы значений
printLists(" Source: ", xSource, ySource)

# ______ используемые узлы интерполяции ______
#
xUsed = [xSource[0], xSource[2], xSource[5], xSource[7], xSource[10]]
yUsed = [ySource[0], ySource[2], ySource[5], ySource[7], ySource[10]]
usedNodesNumber = len(xUsed)
# ____________________________________________

# вывод используемых узлов интерполяции
printLists(" Used nodes: ", xUsed, yUsed)

#testDots = [xSource[0] + 0.5*step, xSource[0] - 0.5*step, xSource[2] + 1.5*step, xSource[2] - 1.5*step, xSource[4] + 1.5*step,
           #xSource[4] - 1.5*step, xSource[6] + 0.5*step, xSource[6] - 0.5*step, xSource[10] + 0.5*step, xSource[10] - 0.5*step]

# __________________________________ main _____________________________________________________

reqX = float(input("\n Enter X: "))
reqY = interpolate(reqX, xUsed, yUsed)

print ("\n The Y is: ", "%8.5f" % reqY, sep = "")


