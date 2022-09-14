#5% bonus if yiu have worked for 5 years or above in a company
x = int(input('Enter You Employee ID'))
print (x)
y = int(input('Enter the year you joined our company'))
salary = int(input('Enter your Salary'))
current_year = 2022
years_Served = current_year - y
#print (years_Served)
if years_Served >= 5:
     print ('Congratulations! Your bonus is:', 0.05*salary)
else:
    print('We are glad to have you. A few more yaers and you will be on board')
         