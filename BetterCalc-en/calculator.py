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

print("Welcome to BetterCalc beta_020421_1000! See all changes in \"changelog\"")

what = input("Operation: (+, -, *, /, ** (expanation), % (mod), // (div), sqrt (√), x! (factorial), rnd (round the number)): ")

print(Back.BLACK)
print(Fore.WHITE)

a = float( input("First number: ") )
b = float( input("Second number: ") )

print(Back.BLACK)
print(Fore.WHITE)

if what == "+":
    c = a + b
    print("Result:" + str(c))
elif what == "-":
    c = a - b
    print("Result:" + str(c))
elif what == "*":
    c = a * b
    print("Result: " + str(c))
elif what == "/":
    c = a / b
    print("Result: " + str(c))
elif what == "**":
    c = a ** b
    print("Result: " + str(c))
elif what == "%":
    c = a % b
    print("Result: " + str(c))
elif what == "//":
    c = a // b
    print("Result: " + str(c))
elif what == "sqrt":
	c = sqrt(a)
	print("Result: " + str(c))
elif what == "x!":
	c = factorial(a)
	print("Result: " + str(c))
elif what == "rnd":
	rnd = input("Round the number to \"floor\" or \"ceil\"?: ")
	if rnd == "floor":
		c = floor(a)
		print("Result: " + str(c))
	elif rnd == "ceil":
		c = ceil(a)
		print("Result: " + str(c))
else:
    print("Operation's inccorect")

input("Press \"Enter\" to close the BetterCalc")