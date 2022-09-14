n= int(input("Enter the value of columns you want to print: "))
for i in range (n):
    for j in range (i+1):
        print ("*", end = " ")
    print()
        #introduce a start condition for the inverse triangle
for i in range (n):
    for j in  range (i,n-1):
        print ("*", end = " ")   
    print()
