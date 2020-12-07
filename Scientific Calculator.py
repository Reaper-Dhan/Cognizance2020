
import math
#Operations that can be done using this calculator
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def product(a,b):
    return a*b
def divide(a,b):
    return a/b
def sqrt(a):
    result=math.sqrt(a)
    return result
def power(a,b):
    return a**b
def mod(a,b):
    return a%b
def exp(a):
    return a**2
def absolute(a):
    result=math.fabs(a)
    return result
def sin(x):
    result=math.sin(x)
    return result
def cos(x):
    result=math.cos(x)
    return result
def tan(x):
    result=math.tan(x)
    return result
def ceil(a):
    result=math.ceil(a)
    return result
def floor(a):
    result=math.floor(a)
    return result
#Choosing the operation to perform
print(""" Choose a number for the following operations.....
 1 - Addition(a,b)
 2 - Subtraction(a,b)
 3 - Multiplication(a,b)
 4 - Division(a,b)
 5 - Square_Root(a)
 6 - Power(a,b) -- Power of 'a' times 'b'
 7 - Remainder(a,b)
 8 - Square(a)
 9 - Absolute(a)
10 - sin(x)
11 - cos(x)
12 - tan(x)
13 - ceil(x)
14 - floor(x) """)
choice=int(input("Enter the number to choose the operation you wanted to perform: "))
#Code for making the calculator
while choice <= 14:
    if choice == 1:
        print("Enter two numbers.....")
        x1=int(input("Enter a: "))
        y1=int(input("Enter b: "))
        result1=add(x1,y1)
        print("The addition of",x1,"and",y1,"is: ",result1)
    elif choice == 2:
        print("Enter two numbers.....")
        x2=int(input("Enter a: "))
        y2=int(input("Enter b: "))
        result2=subtract(x2,y2)
        print("The subtraction of",x2,"and",y2,"is: ",result2)
    elif choice == 3:
        print("Enter two numbers.....")
        x3=int(input("Enter a: "))
        y3=int(input("Enter b: "))
        result3=product(x3,y3)
        print("The product of",x3,"and",y3,"is: ",result3)
    elif choice == 4:
        print("Enter two numbers.....")
        x4=int(input("Enter a: "))
        y4=int(input("Enter b: "))
        result4=divide(x4,y4)
        print("The divison of",x4,"by",y4,"is: ",result4)
    elif choice == 5:
        print("Enter a number.....")
        x5=int(input("Enter a: "))
        result5=sqrt(x5)
        print("The square root of",x5,"is: ",result5)
    elif choice == 6:
        print("Enter two numbers.....")
        x6=int(input("Enter a: "))
        y6=int(input("Enter b: "))
        result6=power(x6,y6)
        print("The power of",x6,"times",y6,"is: ",result6)
    elif choice == 7:
        print("Enter two numbers.....")
        x7=int(input("Enter a: "))
        y7=int(input("Enter b: "))
        result7=mod(x7,y7)
        print("The remainder of",x7,"by",y7,"is: ",result7)
    elif choice == 8:
        print("Enter a number.....")
        x8=int(input("Enter a: "))
        result8=exp(x8)
        print("The square of",x8,"is: ",result8)
    elif choice == 9:
        print("Enter a number.....(integer only)")
        x9=int(input("Enter a: "))
        result9=absolute(x9)
        print("The absolute of",x9,"is: ",result9)
    elif choice == 10:
        x10=int(input("Enter x(in radians): "))
        result10=sin(x10)
        print("sin(x)= ",result10)
    elif choice == 11:
        x11=int(input("Enter x(in radians): "))
        result11=cos(x11)
        print("cos(x)= ",result11)
    elif choice == 12:
        x12=int(input("Enter x(in radians): "))
        result12=tan(x12)
        print("tan(x)= ",result12)
    elif choice == 13:
        x13=float(input("Enter a: "))
        result13=ceil(x13)
        print("The ceil of",x13,"is: ",result13)
    else:
        x14=float(input("Enter a: "))
        result14=floor(x14)
        print("The floor of",x14,"is: ",result14)
    Continue=int(input("Do you like to continue to perform other operation? (YES-->'1')/(NO-->'0') "))
    if Continue == 1:
        choice = int(input("What operation do you like to do next? Please select the number:"))
    elif Continue == 0:
        print("Thanks for using our scientific calculator!!")
        break
    else:
        print("Invalid input")
        break






































