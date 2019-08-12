#   Filename:           Lab 6
#   Created by:         jasongreen
#   Date:               Tuesday, February 12, 2019
#   Time of Creation:   21:26
#   ---

import random

wind_speed = []
high_speed_array = []
low_speed_array = []
average_wind_speed = 0

# need to generate a full array of random numbers between 0 and 30 first.
# Instructions do not say to use random function but lecture video says
# to use it for range between 0 and 30. Change the range iteration to
# (0, 140) to test multiple random generated numbers.
for i in range(0, 14):
    recorded_wind_speed = random.randint(0, 31)
    wind_speed.append(recorded_wind_speed)
    average_wind_speed += wind_speed[i]

# check to see if there are multiple days of high speed recorded
j = 0
print(" ")
print("Max Wind Speed: ", max(wind_speed))
for i in range(len(wind_speed)):
    if wind_speed[i] == max(wind_speed):
        j = i
        j += 1
        high_speed_array.append(j)

# use IF statement to delineate between singular and multiple days recorded
if len(high_speed_array) > 1:
    print("There were multiple days of max wind speeds recorded!\n"
          "They were recorded on days: ", *high_speed_array)
else:
    print("There was only one day of max wind speeds recorded!\n"
          "It was recorded on day: ", *high_speed_array)
print("-" * 20)

# check to see if there are multiple days of low speed recorded
k = 0
print("Min Wind Speed: ", min(wind_speed))
for i in range(len(wind_speed)):
    if wind_speed[i] == min(wind_speed):
        k = i
        k += 1
        low_speed_array.append(k)

# use IF statement to delineate between singular and multiple days recorded
if len(low_speed_array) > 1:
    print("There were multiple days of low wind speeds recorded!\n"
          "They were recorded on days: ", *low_speed_array)
else:
    print("There was only one day of low wind speeds recorded!\n"
          "It was recorded on day: ", *low_speed_array)
print("-" * 20)

# Find the difference between the highest wind speed
# and lowest wind speed

print("The differences of high vs. low wind speed is {} mph!".format(max(wind_speed) - min(wind_speed)))

print("-" * 20)

# Print out the average wind speeds
print("Average wind speed is {:.2f} mph!".format(average_wind_speed / len(wind_speed)))
print("-" * 20)

# Print out the Cardinality of the Wind Speed Array
print("The Cardinality of Set [Wind Speed] is {}.".format(len(wind_speed)))
print("-" * 20)

# For testing purposes, print out the random number generated wind speeds
print("The random number generated wind speeds are:")
print(wind_speed)

# def string_times(var_string):
#     number = 0
#     while number < 3:
#         print(var_string, end="")
#         number += 1
#
#
# var_string = "Hi"
# string_times(var_string)

# r = range(1500, 2700)
# for i in r:
#     if (i % 5 == 0) and (i % 7 == 0):
#         print(i, end=",")

# number = ['10', '27', '23', '12', '81']
# number.reverse()
# print(number)

names = []
ages = []

while True:
    user_input_names = input("Enter a name (type 0 to stop): ")
    if user_input_names.strip() == "0":
            print("You have exited the program!")
            break
    user_input_ages = input("Enter an age: ")

    ages.append(user_input_ages)
    names.append(user_input_names)

for i in range(len(names)):
    print(names[i], ages[i])



