# Write a Python program
#to find those numbers which are divisible by 7 and multiple of 5,
#between 1500 and 2700 (both included).

def isMultiple(num,  check_with):
    return num % check_with == 0;
numbers2 = range (1500, 2701)
for j in numbers2:
    if (isMultiple(j, 5) == True ) and j % 7 == 0:
        print(j);

#Write a Python program to convert temperatures to and from celsius, fahrenheit.
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
#Expected Output :
#60°C is 140 in Fahrenheit
#45°F is 7 in Celsius
prompt1= int(input("Press 1 if you want to convert temperature from Fahrenheit to Celsius. Else Press 2 "))

if prompt1 == 1:
    Fahrenheit = int(input('Enter the temperature you wish to convert to Celsius:'))
    Celsius = int((Fahrenheit-32)*5)//9
    print ("The temperature in Celsius is :", Celsius, "degreess.")
elif prompt1 == 2:
    x = int(input('Enter the temperature you wish to convert Fahrenheit:'))
    y= int((x*9)/5) + 32
    print ("The temperature in Fahrenheit is ", y, "degreess.")
else:
    print("Invalid input")