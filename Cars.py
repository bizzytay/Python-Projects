#Taylor Herrera 2/12/2017
#Requires data.txt file

"""Read in a file of cars with json and categorize each car. Calculates the average of the odometer."""


import json

#class car that has attributes of year, make, odometer and the status
class car:
    def __init__(self,year=0,make="",odometer=0):
        self._year = year
        self._make = make
        self._odometer = odometer
        self._status = ""

	#this is how the car will be displayed
    def __repr__(self,y,m,o,s):
        print "Year:",y,"Make",m,"Odometer:",o,"Status",s
	#gets the year of the car and returns the value
    def get_year(self):
        return self._year
	#gets the make of the car and returns the value
    def get_make(self):
        return self._make
	#gets the odometer of the car and returns the value
    def get_odometer(self):
        return self._odometer
	#gets the the of the car and returns the value and decides whether
    def get_status(self):
        if self._odometer < 50000:
            return "NEW"
        elif self._odometer < 150000:
            return "USED"
        else:
            return "JUNK"


# opens and read the data.txt which is a file that constains a list of cars
fp = open("data.txt",'r')
s = fp.read()
jin = json.loads(s)
#calculates total odometer
average = 0.0
#to calculate the length of the odometer
l = []
make = []
status = []

#for every item within jin, create a car object and find the attributes that are year, make, and the odometer. 
for i in jin:
    c = car(i["year"],i["make"],i["odometer"])
	#this is to calculate the average of the odometer
    average += i["odometer"]
    l.append(i["odometer"])
    make.append(i["make"])
    status.append(c.get_status())
	#send the year, make, odometer, and status with getters so the information can be displayed
    c.__repr__(c.get_year(),c.get_make(),c.get_odometer(),c.get_status())

#finds the most frequent car using the max function
most_cars = max(make,key=lambda x: make.count(x))

#find the least car using min function
least_cars = min(make,key=lambda x: make.count(x))

#most common status found
most_status = max(status,key=lambda x: status.count(x))

print "Average is: ", average/len(l)
print "Most Common Car:", most_cars
print "Least Common Car:", least_cars
print "Most Common Status:", most_status
