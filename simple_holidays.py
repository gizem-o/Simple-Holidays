# -- Program to calculate the total cost of holiday, depending on 5 different cities -- #

# Checking to see if one of the 5 cities are picked
def city_flight_checker(x):
    while x < 1 or x > 5:
        print("Sorry, this is not one of the options.")
        x = int(input("Please enter the number of the city you would like to visit: "))
    return x 

print("City options:\n1. Paris\n2. Rome\n3. Madrid\n4. Amsterdam\n5. Athens")
city_flight_variable = int(input("Please enter the number of the city you would like to visit: "))
city_flight_variable = city_flight_checker(city_flight_variable)   # Checking if input is one of the options

num_nights_variable = int(input("Please enter the number of nights you would like to stay: "))

rental_days_variable = int(input("Please enter the number of days you would like to rent a car: "))

def hotel_cost(city_flight, num_nights):     # Would be less confusing to read if using different argument name to variable
# The cost of the hotel per night is dependant on the city chosen
    if city_flight == 1:
        cost_per_night = 115
    elif city_flight == 2:
        cost_per_night = 98
    elif city_flight == 3:
        cost_per_night = 76
    elif city_flight == 4:
        cost_per_night = 85
    elif city_flight == 5:
        cost_per_night = 104
    return cost_per_night * num_nights

def plane_cost(city_flight):
# The cost of the plane is dependant on the city chosen
    if city_flight == 1:
        plane_cost = 120
    elif city_flight == 2:
        plane_cost = 82
    elif city_flight == 3:
        plane_cost = 60
    elif city_flight == 4:
        plane_cost = 75
    elif city_flight == 5:
        plane_cost = 105
    return plane_cost

def car_rental(city_flight, rental_days):
# The cost of the car rental is dependant on the city chosen
    if city_flight == 1:
        car_cost = 122
    elif city_flight == 2:
        car_cost = 17
    elif city_flight == 3:
         car_cost = 36
    elif city_flight == 4:
        car_cost = 158
    elif city_flight == 5:
        car_cost = 28
    return rental_days * car_cost

def holiday_cost(num_nights, city_flight, rental_days):     # Mistake in task asking us to have functions as arguments
    total_hotel = hotel_cost(city_flight, num_nights)
    total_plane = plane_cost(city_flight)
    total_car = car_rental(city_flight, rental_days)
    return total_hotel + total_plane + total_car    # Adding all the costs

print("The total cost of this holiday is: £" + str(holiday_cost(num_nights_variable, city_flight_variable, rental_days_variable)))