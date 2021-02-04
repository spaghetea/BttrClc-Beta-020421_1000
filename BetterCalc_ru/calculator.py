# use Colorama to make Termcolor work on Windows too use init()
from colorama import init
from colorama import Fore, Back, Style
from math import sqrt
from math import factorial
from math import floor
from math import ceil


init()

print(Back.BLACK)
print(Fore.WHITE)

print("Добро пожаловать в BetterCalc beta_020421_1000! Смотрите все изменения в \"changelog\"")

what = input("Операция: (+, -, *, /, ** (степень), % (остаток при делении), // (целое число при делении), корень (√), x! (факториал), rnd (округлить число)): ")

print(Back.BLACK)
print(Fore.WHITE)

a = float( input("Первое число: ") )
b = float( input("Второе число: ") )

print(Back.BLACK)
print(Fore.WHITE)

if what == "+":
    c = a + b
    print("Результат:" + str(c))
elif what == "-":
    c = a - b
    print("Результат:" + str(c))
elif what == "*":
    c = a * b
    print("Результат: " + str(c))
elif what == "/":
    c = a / b
    print("Результат: " + str(c))
elif what == "**":
    c = a ** b
    print("Результат: " + str(c))
elif what == "%":
    c = a % b
    print("Результат: " + str(c))
elif what == "//":
    c = a // b
    print("Результат: " + str(c))
elif what == "корень":
    c = sqrt(a)
    print("Результат: " + str(c))
elif what == "x!":
    c = factorial(a)
    print("Результат: " + str(c))
elif what == "rnd":
    rnd = input("Округлить число в пользу меньшего числа (пишите: \"пол\") или большего числа? (пишите: \"потолок\")?: ")
    if rnd == "пол":
        c = floor(a)
        print("Результат: " + str(c))
    elif rnd == "потолок":
        c = ceil(a)
        print("Результат: " + str(c))
else:
    print("Неверная операция")

input("Нажмите \"Enter\", чтобы закрыть BetterCalc")