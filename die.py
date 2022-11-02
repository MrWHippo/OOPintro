from functools import total_ordering
from random import randrange


class die:
    __serialnumber = 1000
    def __init__(self, numfaces):
        self.__numfaces = numfaces
        self.__serialnumber = die.__serialnumber
        die.__serialnumber += 1

    def getnumfaces(self):
        print(f"Number of faces: {self.__numfaces}")
        return self.__numfaces

    def roll(self):
        self.__value = randrange(self.__numfaces)
        return self.__value
    
    def getvalue(self):
        return self.__value
    
    def setvalue(self, newvalue):
        if newvalue > self.__numfaces or newvalue <= 0:
            print("Value outside of range")
        else:
            self.__value = newvalue
    
    def getserialnumber(self):
        return self.__serialnumber

class DiceSet:
    def __init__(self):
        self.diceset = []
    
    def addDie(self, DIE):
        self.diceset.append(DIE)
    
    def rollall(self):
        for DIE in self.diceset:
            total += DIE.roll()
        return total
    
    def displayTotal(self):
        


die1 = die(6)

while True:
    numberoffaces = input("Enter the number of faces or enter '#' to exit or '-' to change value of die: ")
    if numberoffaces == "#":
        break
    elif numberoffaces == "-":
        newvalue = int(input("Enter new value of die: "))
        die1.setvalue(newvalue)
        print("New Value: ",die1.getvalue())
    else:
        die1 = die(int(numberoffaces))
        die1.getnumfaces()
        serialnum = die1.getserialnumber()
        print("Value: ",die1.roll(),f"(serial number {serialnum})")
    










