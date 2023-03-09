n1 = 0
n2 = 0
oper = ""
x = 0
num = float(input("Введите количество операций\n"))

i = 0
n1 = float(input("Введите первое число\n"))
n2 = float(input("Введите второе число\n"))
oper = input("Введите операцию 1-сложение 2-вычетания 3- умножение 4-деление\n")
if oper == 1:
    x = n1+n2
elif oper == 2:
    x = n1-n2
elif oper ==3:
    x = n1*n2
elif oper ==4:
    x= n1/n2
    if n2 == 0:
        print("На ноль делить нельзя")

while i != num:
    n2 = float(input("Введите число"))
    oper = float(input("Введите операцию 1-сложение 2-вычетания 3- умножение 4-деление\n"))
    match oper: 
        case 1:
            x = n1+n2
        case 2:
            x = n1-n2
        case 3:
            x = n1*n2
        case 4:
            x= n1/n2
print(x)