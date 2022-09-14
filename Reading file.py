#Reading a file
import math

#with open('test.txt') as test_text:
#    reader = test_text.read()
#    print (reader)

def file_read(fname = str(input("Enter the name of the text file you want to open:"))):
        txt = open(fname)
        print(txt.read())
        txt.close()
        

file_read()

#I liked this exercise. It helped think and implement my own ideas
#I did not wish to hard code this excercise, and I managed. Huree! Bravo!
return dir()