class  Time(object):

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(t1, t2):
        t3 = Time(0, 0) # creating new object
        t3.hours = t1.hours + t2.hours # sum of hours
        t3.minutes = t1.minutes + t2.minutes # sum of minutes
        while t3.minutes >= 60:
            t3.hours += 1
            t3.minutes -= 60
        return t3

    def displayTime(self):
        print("Time is %d hours and %d minutes" %(self.hours, self.minutes))

    def displayMinutes(self):
        print("Total time in minutes is: ", (self.hours * 60) + self.minutes, "minutes")
hours1 = (int(input("Enter the first hour you want to add: ")))
minutes1 = (int(input("Enter the first minutes you want to add: ")))

hours2 = (int(input("Enter the second hours  you want to add: ")))
minutes2 = (int(input("Enter the second minutes you want to add: ")))
a = Time(hours1, minutes1)
b = Time(hours2, minutes2)
c = Time.addTime(a,b)

c.displayTime()
c.displayMinutes()

#input()

#adding dictionary
print("This is the update of dictonaries code:")
f = {0:10, 1:20}
print(f)
f.update({2:30})
print(f)

input()