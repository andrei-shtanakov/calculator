# -*- cod# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 08:17:58 2019
Продолжение работы с Git
дключение из PyCharm

Спрашиваем число X, затем второе число Y, затем оператор.
Выполняем действие и сохраняем результат в первой переменной X, 
запрашиваем опять 2-е число Y и оператор, 
выполняем действие и сохраняем в первой переменной X. 
И так далее...

@author: Andrei Shtanakov
"""

class trivial_calculator(object):
    def __init__(self):
        """Constructor"""
        self.x = 0
        self.y = 0
        self.res = 0
        self.operator = ""
        self.cicl = True
        
    def inspection(self, x):
        try:
            x = float(x)
            return True
        except ValueError:
            print("Неверное значение!")
            return False
    
    def inspectoper(self, op):
        if op in ['-','+','/','*','q']:
            return True
        else:
            return False
        
        
    def operators(self, oper):
        if oper == "+":
            self.res = self.x + self.y
            print ("X = X + Y = ", self.x, " + ", self.y, " = ", self.res)
            self.x = self.res
        elif oper == "-":
            self.res = self.x - self.y
            print ("X = X - Y = ", self.x, " - ", self.y, " = ", self.res)
            self.x = self.res
        elif oper == "*":
            self.res = self.x * self.y
            print ("X = X * Y = ", self.x, " * ", self.y, " = ", self.res)
            self.x = self.res
        elif oper == "/":
            try:
                self.res = self.x / self.y
                print ("X = X / Y = ", self.x, " / ", self.y, " = ", self.res)
                self.x = self.res
            except ZeroDivisionError:
                print ("На 0 делить нельзя!")
        elif oper == "q":
            self.cicl = False
        else:
            pass

        
    def calc(self):
        print("Выход из цикла при вводе 'q' вместо оператора")
        while self.cicl:
            x = 0
            op = ""
            flag = False
            while flag == False:
                x = input("Введите число X: ")
                flag = self.inspection(x)
            self.x = float(x)
            flag = False
            while flag == False:
                x = input("Введите число Y: ")
                flag = self.inspection(x)
            self.y = float(x)
            flag = False
            while flag == False:
                op = input("Введите оператор: ")
                flag = self.inspectoper(op)
#            self.operator = op
            self.operators(op) 

my_calc = trivial_calculator()

my_calc.calc()