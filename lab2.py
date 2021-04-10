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

    def interpolate(self, requiredX):
        
        # первый полином
        if (math.fabs(requiredX - self.xLeft) < math.fabs(requiredX - self.xRight)):
            
            result = self.y[0]

            # итерация цикла - одно слагаемое полинома
            for k in range(1, self.valuesNumber):
                a = self.diffs[k - 1][0] / math.factorial(k) / self.step**k

                for i in range(k):
                    a *= requiredX - self.x[i]

                result += a

        # второй полином
        else:
            
            result = self.y[self.valuesNumber - 1]

            # итерация цикла - одно слагаемое полинома
            for k in range(self.valuesNumber - 2, 0, - 1):
                nowIndex = self.valuesNumber - 1 - k

                a = self.diffs[nowIndex - 1][k] / math.factorial(nowIndex) / self.step**nowIndex

                for i in range(self.valuesNumber - 1, k, -1):
                    a *= requiredX - self.x[self.valuesNumber - 1]

                result += a

        return result
    
    def printDiffs(self):
        for i in range(len(self.diffs)):
            print("dY[", i + 1, "]      ", sep = "", end = "")
        print()
        
        for i in range(len(self.diffs)):
            for j in range(len(self.diffs[i])):
                print("%-11.6f" % self.diffs[j][i], sep = "", end = "")
            print()
        print()
        
# main
            
one = Lab()
one.printDiffs()
#arg = float(input(" Enter argument: "))
#print(math.e**math.sin(arg))
#print(one.interpolate(arg))

print("X", "Ftrue", "FN", "mis", sep = "       ")
args = [-0.18, 0.18, -0.45, 0.45, 0.775, 1.225, 0.55, 1.45]

for i in range(len(args)):
    print(args[i], "%.6f" % one.function(args[i]), "%.6f" % one.interpolate(args[i]), "%.6f" % math.fabs(one.function(args[i]) - one.interpolate(args[i])), sep = "  ")