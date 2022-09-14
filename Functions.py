#Functions
#quiz 1 
def simpleInterest():
    principal=int(input('Enter the principal amount: '))
    rate=int(input('Enter the rate:'))
    time=int(input('Enter the amount of time in years: '))
    #simple interest
    s=1 + rate*time
    p = principal * s
    return p

print('The simple interest is:',simpleInterest())

#Quiz
def sum():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a + b
    if c in range(15,21):
        print(20)
    else:
        print(c)
   
sum()

#quiz 4
#Area and perimeter
def areaPerimeter():
    a = int(input("Enter the length of a rectangle: "))
    b = int(input("Enter the width of the rectangle: "))
    c = a + b
    d = a*b
    print("The area is ", d ,"and the perimetr is ", c)
areaPerimeter()
