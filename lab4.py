import math

class Lab:
    def function(self, requiredX):
        return math.e  ** math.sin(requiredX)
        #return math.tan(requiredX**3)

    x = [] # лист аргументов
    y = [] # лист значений функции
    
    xRight = 1.0   # правая граница
    xLeft = 0.0    # левая граница
    valuesNumber = 10 + 1 # количество узлов
    step = (xRight - xLeft) / valuesNumber # интервал между узлами

    diffs = []

    def __init__(self):
        # для большей точности - шаг 1.1
        self.step += self.step / self.valuesNumber

        self.x.append(self.xLeft) # первое значение X
        self.y.append(self.function(self.x[0])) # первое значение Y 

        # заполнение функции
        for i in range(1, self.valuesNumber):
            self.x.append(self.x[i - 1] + self.step) # X
            self.y.append(self.function(self.x[i]))  # Y

        # генерация таблицы разностей
        #
        # заполнение первого листа
        self.diffs.append([0.0] * (self.valuesNumber - 1)) 
        for i in range(self.valuesNumber - 1):
            self.diffs[0][i] = self.y[i + 1] - self.y[i]

        # заполнение остальных листов
        for diffLen in range(self.valuesNumber - 2, 0, -1):
            # создание списка (разности k порядка)
            self.diffs.append([0.0] * diffLen)
            
            # для всех разностей этого порядка
            for i in range(diffLen):
                nowIndex = self.valuesNumber - 1 - diffLen

                # заполнение разностей
                self.diffs[nowIndex][i] = self.diffs[nowIndex - 1][i + 1] - self.diffs[nowIndex - 1][i]

                # вывод разностей
                #print("%.5f" % self.diffs[self.valuesNumber - 1 - diffLen][i], end = " ")
            #print()

    def differentiate_first(self, requiredX):
        return (self.function(requiredX + self.step) - self.function(requiredX)) / self.step
        
    def differentiate_second(self, requiredX):
        return((self.differentiate_first(requiredX + self.step) - self.differentiate_first(requiredX)) / self.step) 
    
    def printDiffs(self):
        for i in range(len(self.diffs)):
            print(" dY[", i + 1, "]      ", sep = "", end = "")
        print()
        
        for i in range(len(self.diffs)):
            for j in range(len(self.diffs[i])):
                print("%-11.6f" % self.diffs[j][i], sep = "", end = "")
            print()
        print()
        
# main
            
one = Lab()
one.printDiffs()
print(one.differentiate_first(0.2))
print(one.differentiate_second(0.2))
