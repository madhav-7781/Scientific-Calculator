# Scientific-Calculator

import math
print("""
press -
1 - Addition(x,y)
2 - Subtraction(x,y)
3 - Multiplication(x,y)
4 - Division(x,y)
5 - Exponent(x,y)
6 - tangent(x)
7 - sine(x)
8 - cosine(x)
9 - factorial(x)
10 - log(x)
""")
o = input(" ")
print()
if o == "1":
    x = float(input("Enter 1st Number: "))
    y = float(input("Enter 2nd Number: "))
    print(x+y) #addition
elif o == "2":
    x = float(input("Enter 1st Number: "))
    y = float(input("Enter 2nd Number: "))
    print(x-y) #subtraction
elif o == "3":
    x = float(input("Enter 1st Number: "))
    y = float(input("Enter 2nd Number: "))
    print(x*y) #Multiplication
elif o == "4":
    x = float(input("Enter 1st Number: "))
    y = float(input("Enter 2nd Number: "))
    print(x/y) #Division
elif o == "5":
    x = float(input("Enter 1st Number: "))
    y = float(input("Enter 2nd Number: "))
    print(x^y) #Exponent
elif o == "6":
    x = float(input("Enter a Number: "))
    print(math.tan(x)) #tangent
elif o == "7":
    x = float(input("Enter a Number: "))
    print(math.sin(x)) #sine
elif o == "8":
    x = float(input("Enter a Number: "))
    print(math.cos(x)) #cosine
elif o == "9":
    x = float(input("Enter a Number: "))
    print(math.factorial(x)) #factorial
elif o == "10":
    x = float(input("Enter a Number: "))
    print(math.log(x)) #log
