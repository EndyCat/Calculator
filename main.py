from colorama import init
from colorama import Fore, Back, Style

init()
print(Back.CYAN)
print(Fore.BLACK)
print('Приветствую в калькуляторе!')
x0 = str(input("Укажите действие которое хотите совершить (Укажите цифру рядом с которой стоит знак!)\n1. + (Плюс)\n2. - (Минус)\n3. *(Умножить)\n4. / (Делить)\n: "))
print(Back.YELLOW)
num1 = int(input("Введите первое число:"))
print(Back.RED)
num2 = int(input("Введите второе число:"))
print(Back.GREEN)
print("Ответ: ")
if "1" in x0:
    x1 = int(num1) + int(num2)
    print(x1)
elif "2" in x0:
    x2 = int(num1) - int(num2)
    print(x2)
elif "3" in x0:
    x3 = int(num1) * int(num2)
    print(x3)
elif "4" in x0:
    x4 = int(num1) / int(num2)
    print(x4)
else:
    print(Back.BLUE)
    print("Указаный знак не является верным, пожалуйста при вводе знака пишите число под которым он!")
kkj = input()
