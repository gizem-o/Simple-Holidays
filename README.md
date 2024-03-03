# Holiday Cost Calculator

This Python program calculates the total cost of a holiday based on the city chosen, the number of nights to stay, and the rental days for a car. The costs include hotel stay, plane tickets, and car rental.

## Features

- Select from 5 different cities: Paris, Rome, Madrid, Amsterdam, Athens.
- Input the number of nights you would like to stay.
- Input the number of days you would like to rent a car.
- Calculates the cost of the hotel stay, plane tickets, and car rental.
- Provides the total cost of the holiday.

## Usage

1. Run the program.
2. Choose the desired city from the available options.
3. Input the number of nights you plan to stay.
4. Input the number of days you want to rent a car.
5. Get the total cost of the holiday.

## City Options

1. Paris
2. Rome
3. Madrid
4. Amsterdam
5. Athens

## Functions

### `city_flight_checker(x)`

- Checks if the entered city option is within the available options.
- Asks the user again if not within options.

### `hotel_cost(city_flight, num_nights)`

- Multiplies the hotel cost per night with the number of nights entered.

### `plane_cost(city_flight)`

- Returns the cost of the plane ticket based on the chosen city.

### `car_rental(city_flight, rental_days)`

- Multiplies the car cost per day with the number of days entered.

### `holiday_cost(num_nights, city_flight, rental_days)`

- Adds the cost of hotel stay, plane tickets, and car rental to calculate the total holiday cost.
