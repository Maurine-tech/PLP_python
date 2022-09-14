#To add 2 posotive numbers without using an + sign
#I am using the and operator 
a = 2 & 3

#Now am using the or operator
b = 2|5
# Now am using the XOR operator
c = 4 ^ 5
print(a, b,c)
#Python program to check the priority of the four operators (+, -, *, /).
from collections import deque
import re

operators = "+ - * /"
parathesis = "()"
priority = {
    '+':0,
    '-':0,
    '*':1,
    '/':1,
    }
def test_higher_priority (operator1, operator2):
    return priority[operator1] >= priority[operator2]
print (test_higher_priority('+','*'))
print (test_higher_priority('-','*'))
print (test_higher_priority('/','*'))
print (test_higher_priority('*','/'))
print (test_higher_priority('+','-'))
print (test_higher_priority('-','/'))

#I have learnt that * has the highest priority,
#followed by + then / and finally - 