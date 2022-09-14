#Assignment 1
x = int(input('Enter your marks'))
if x > 70 and x <= 100:
    print("Your grade is A")
elif x >60 and x <= 69:
    print ("Your Grade is B")
elif x > 50 and x <=59:
    print("Your Grade is C")
else:
    print("You failed your exam! You got an E")
    
 #Assignment 2
y = int(input("Enter the Quantity you want to buy"))
cost = y*100

if cost >= 1000:
    print("Your cost is:", cost ,"and your bonus is:", 0.1*cost)
else:
    print("Your cost is:", cost, "but we are sorry you did not get a bonus.")
    