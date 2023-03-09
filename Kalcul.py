n1 = 0
oper1 = ""
n2 = 0
oper2 = ""
n3 = 0
oper3 = ""
n4 = 0 
oper4 = ""
n5 = 0
oper5 = ""
n6 = 0
x=0

n1 = float(input("Введите первое число\n"))
n2 = float(input("Введите второе число\n"))
oper1 = input("Введите операцию +(плюс) -(минус) *(умножить) /(делить)\n")
if oper1 == "+":
    print("%.2f" % (n1+n2))
    x = n1+n2
elif oper1 == '-':
    print("%.2f" % (n1-n2))
    x = n1-n2
elif oper1 == '*':
    print("%.2f" % (n1*n2))
    x = n1*n2
elif oper1 == '/':
    print("%.2f" % (n1/n2))
    x = n1/n2
else:
        print("Неверный знак операции!")
n3 = float(input("Введите следуюзее число\n"))
oper2 = input("Введите операцию +(плюс) -(минус) *(умножить) /(делить)\n")
if oper2 == "+":
    print("%.2f" % (x+n3))
    x = x+n3
elif oper2 == '-':
    print("%.2f" % (x-n3))
    x = x-n3
elif oper2 == '*':
    print("%.2f" % (x*n3))
    x = x*n3
elif oper2 == '/':
    print("%.2f" % (x/n3))
    x = x/n3
    if n3 == 0:
        print("На ноль делить нельзя")
else:
        print("Неверный знак операции!")
n4 = float(input("Введите следуюзее число\n"))
oper3 = input("Введите операцию +(плюс) -(минус) *(умножить) /(делить)\n")
if oper3 == "+":
    print("%.2f" % (x+n4))
    x = x+n4
elif oper3 == '-':
    print("%.2f" % (x-n4))
    x = x-n4
elif oper3 == '*':
    print("%.2f" % (x*n4))
    x = x*n4
elif oper3 == '/':
    print("%.2f" % (x/n4))
    x = x/n4
else:
        print("Неверный знак операции!")


n5 = float(input("Введите следуюзее число\n"))
oper4 = input("Введите операцию +(плюс) -(минус) *(умножить) /(делить)\n")
if oper4 == "+":
    print("%.2f" % (x+n5))
    x = x+n5
elif oper4 == '-':
    print("%.2f" % (x-n5))
    x = x-n5
elif oper4 == '*':
    print("%.2f" % (x*n5))
    x = x*n5
elif oper4 == '/':
    print("%.2f" % (x/n5))
    x = x/n5
else:
        print("Неверный знак операции!")

n6 = float(input("Введите следуюзее число\n"))
oper5 = input("Введите операцию +(плюс) -(минус) *(умножить) /(делить)\n")
if oper5 == "+":
    print("%.2f" % (x+n6))
    x = x+n6
elif oper5 == '-':
    print("%.2f" % (x-n6))
    x = x-n6
elif oper5 == '*':
    print("%.2f" % (x*n6))
    x = x*n6
elif oper5 == '/':
    print("%.2f" % (x/n6))
    x = x/n6
else:
        print("Неверный знак операции!")
