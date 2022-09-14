#This code asks user to input name and tel No.
#Useful link: https://iq.opengenus.org/capitalize-letters-in-python/#:~:text=To%20capitalize%20the%20first%20letter,copy%20of%20the%20modified%20string.

Name=input("Enter Your Two Names:").lower()
Phone_Number=input("Enter Your Phone Number:")
print("You entered:", Name,"in lowercase.")
Capitalized_Name= Name.title()# title() capitalizes each word. ( puts then in title case). 
print("Your Capitalized Name is:", Capitalized_Name,".")
Spliting_Names=Name.split()
first_Name=Spliting_Names[0]
second_Name=Spliting_Names[1]
# print(Your first name is:- {first_Name}, and your second name is: - {second_Name})
print(f" {first_Name}  {second_Name}")
print(f"Your name is {Capitalized_Name} and your phone number is {Phone_Number}")
