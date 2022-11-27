from math import*

#Задание 1
a=int(input("Введите число: "))
if a>0:
    text="положительное"
    if a % 2 == 0:
        text += ", четное"
    else:
        text += ", нечетное"
elif a==0:
    text="неопределенное"
else:
    text="отрицательное"
print(f"{a} - {text} число")

#Задание 2
try:
    a=float(input("Введите первое число> "))
    b=float(input("Введите второе число> "))
    c=float(input("Введите третье число> "))
    if a>0 and b>0 and c>0:
        print("числа положительные")
        if a+b+c==180:
            print("треугольник получится:", end=" ")
            if a==b==c:
                print("равносторонний\n")
            elif a==b or b==c or a==c:
                print("равнобедренный\n")
            elif a!=b!=c:
                 print("разносторонний\n")
            if a==90 or b==90 or c==90:
                print("прямоугольный\n")
        else:
            print("треугольник не получится")
    else:
        print("значения недопустимы")
except ValueError:
    print("Vale! ")

#Задание 3
print("Хотите ли вы расшифровать порядковый номер дня недели в название?")
a=str(input("=> "))
if a.lower()=="да":
    print("Введите число от 1 до 7");b=int(input("Введите число> "))
    if b==1:
        print("Понедельник")
    elif b==2:
        print("Вторник")
    elif b==3:
        print("Среда")
    elif b==4:
        print("Четверг")
    elif b==5:
        print("Пятница")
    elif b==6:
        print("Суббота")
    elif b==7:
        print("Воскресенье")
else:
    print("Вы не хотите расшифровать порядковый номер дня недели или ввели неправильное значение")

#Задание 4
try:
    date=int(input("Введите день рождения:"))
    month=int(input("Введите месяц рождения:"))
    year=int(input("Год:"))
    if year%4==0:
        print("Veebruasis 29 päevad, liigaasta")
    else:
        print("Veebruasis 28 päevad, liigaasta")
    if (month in [1,3,5,7,8,10,12] and date>0 and date<=31 or month [4,5,9,11] and date>0 and date<=30):
        if (date>20 and date<=31 and month==3) or( month==4 and date<=19):
           print("Знак зодиака:Овен")
        elif (date<=30 and month==4) or( month==5 and date<=20):
           print("Знак зодиака:Телец")
        elif (date<=31 and month==5) or( month==6 and date<=21):
           print("Знак зодиака:Близнецы")
        elif (date<=30 and month==6) or( month==7 and date<=22):
           print("Знак зодиака:Рак")
        elif (date<=31 and month==7) or( month==8 and date<=22):
           print("Знак зодиака:Лев")
        elif (date<=31 and month==8) or( month==9 and date<=22):
           print("Знак зодиака:Дева")
        elif (date<=30 and month==9) or( month==10 and date<=23):
           print("Знак зодиака:Весы")
        elif (date<=31 and month==10) or( month==11 and date<=22):
           print("Знак зодиака:Скорпион")
        elif (date<=30 and month==11) or( month==12 and date<=21):
           print("Знак зодиака:Стрелец")
        elif (date<=31 and month==12) or( month==1 and date<=20):
           print("Знак зодиака:Козерог")
        elif (date<=31 and month==1) or( month==2 and date<=18):
           print("Знак зодиака:Водолей")
        elif (date<=29 and month==2) or( month==3 and date<=20):
           print("Знак зодиака:Рыбы")
        else:
            print("Неверный ввод даты")
except ValueError:
    print("Неверный ввод! ")

#Задание 5
n=input("Введите число: ")
while 1 : 
    try:
        if isinstance(int(n), int):
            print("int: ",int(n)*0.5)
            break
    except:
        pass
    try:
        if isinstance(float(n), float):
            print("float: ",float(n)*0.7)
            break
    except:
        pass
    try:
        if n.isalpha():
            print("string: ",n)
            break
    except:
        pass

#Задание 6
try:
    print("Введите коэффициенты a, b, c, где коэффициент а не равен 0")
    a=float(input("a=> "))
    b=float(input("b=> "))
    c=float(input("c=> "))
    D=b**2-4*a*c 
    if D<0:
        print("Нет решения")
    elif D==0:
        x=(-1*b+sqrt(D))/(2*a)
        print("Уравнение имеет одно решение:", x)
    else:
        x1=(-1*b+sqrt(D))/(2*a)
        x2=(-1*b-sqrt(D))/(2*a)
        print("Уравнение имеет два решения:", round(x1,2), "и", round(x2,2))
except ValueError:
    print("Неверный ввод")