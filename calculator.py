# -*- cod# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 08:17:58 2019

Спрашиваем число X, затем второе число Y, затем оператор.
Выполняем действие и сохраняем результат в первой переменной X, 
запрашиваем опять 2-е число Y и оператор, 
выполняем действие и сохраняем в первой переменной X. 
И так далее...

@author: Andrei Shtanakov
"""


print("Выход из цикла при вводе 'q' вместо числа Y или вместо оператора")
x = input("Введите число X: ")

# Проверка на правильность ввода числа X
try:
    x = float(x)
except ValueError:
    print("Неверное значение X!")
    print("X присвоено значение 0")
    x = 0

y = 1
while y != "q":
    y = input("Введите число Y: ")
    oper = 0
    if y == "q":
        continue
    else:

        # Проверка на правильность ввода числа Y
        try:
            y = float(y)
#        y = float(y)
        except ValueError:
            y = 0
            oper = "+"
            print("Неверное значение Y!")
            continue

        while oper == 0:
            oper = input("Введите оператор: ")
            if oper == "+":
                print ("X = X + Y = ", x, " + ", y, " = ", x + y)
                x += y
            elif oper == "-":
                print ("X = X - Y = ", x, " - ", y, " = ", x - y)
                x -=y
            elif oper == "*":
                print ("X = X * Y = ", x, " * ", y, " = ", x * y)
                x *= y
            elif oper == "/":
                try:
                    print ("X = X - Y = ", x, " / ", y, " = ",  x / y)
                except ZeroDivisionError:
                    print ("На 0 делить нельзя!")
            elif oper == "q":
                y = "q"
            else:
                print("Неверный оператор!")
                oper = 0
            
            
        
    