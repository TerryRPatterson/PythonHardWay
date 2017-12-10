#Number of cars available
cars = 100
#Number of people a car can hold
space_in_a_car = 4.0
#Number of drivers available
drivers = 30
#Number of passengers total
passengers = 90
#Calculating number of idle cars
cars_not_driven = cars - drivers
#Calculating number of cars in use
cars_driven = drivers
#Calculating number of passengers carpool can move
carpool_capacity = cars_driven * space_in_a_car
#Calculating average passengers in each car
average_passengers_per_car =  passengers / cars_driven

#Giving user output
print("There are", cars, "cars available.")
print("There are only", drivers,"drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
#Study Drill output:
#The variable name is incorrect car_pool_capacity should be carpool_capacity
#Python was saying that the variable you were trying to call had not been given
# a value.
