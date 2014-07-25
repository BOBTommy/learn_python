__author__ = 'riskkim'
#All car enrolled
cars = 100
#Spaces in one car. It means that there are 4 seats in a car.
space_in_a_car = 4.0
#Persons who can drive a car
drivers = 30
#Persons who want to get a car
passengers = 90
#Cars are not work
cars_not_driven = cars - drivers
#Cars are now outside.
cars_driven = drivers
#Seats available
carpool_capacity = cars_driven * space_in_a_car
#Average of passengers in a car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
