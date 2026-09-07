   #Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
   #Write a python comment saying 'Day 2: 30 Days of python programming'
   #  Declare a first name variable and assign a value to it
   #  Declare a last name variable and assign a value to it
   #  Declare a full name variable and assign a value to it
   #  Declare a country variable and assign a value to it
   #  Declare a city variable and assign a value to it
   #  Declare an age variable and assign a value to it
   #  Declare a year variable and assign a value to it
   #  Declare a variable is_married and assign a value to it
   #  Declare a variable is_true and assign a value to it
   #  Declare a variable is_light_on and assign a value to it
   #  Declare multiple variable on one line

# Write a python comment saying 'Day 2: 30 Days of python programming
first_name = "Ben"
last_name = "Okabayashi"
full_name = first_name + " " + last_name
country = "USA"
city = "Seattle"
age = 25
year = 2026

is_married = False
is_true = True
is_light_on = False

# Declare multiple variables on one line
x, y, z = 1, 2, 3

# print(type(first_name))
# print(type(last_name))
# print(type(full_name))
# print(type(country))
# print(type(city))
# print(type(age))
# print(type(year))
# print(type(is_married))
# print(type(is_true))
# print(type(is_light_on))
# print(type(x))
# print(type(y))
# print(type(z))
# print(first_name)

#2
len_first_name = len(first_name)
print(len_first_name)

#3
print(len_first_name," ", len(last_name))

#4
num_one= 5
num_two=4

#5
variable_total= num_one +num_two
print(variable_total)

#6
variable_diff = num_one - num_two

#7
variable_product = num_one * num_two

#8
variable_division = num_one / num_two

#9
variable_remainder = num_one // num_two

#10
variable_exp = num_one ** num_two
print(variable_diff, variable_product, variable_division, variable_remainder, variable_exp)

#11
floor_division = num_one // num_two
print(floor_division)

#12
#a)
rad_of_circle = 30 
area_of_circle= 3.14 * rad_of_circle**2

#b)
circumference_of_circle = 2*3.14* rad_of_circle

#c)
user_radius = float(input("Enter the radius: "))
user_area = 3.14159 * user_radius ** 2
print(user_area)


# 13. Get user input for first name, last name, country, age
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")
print(first_name, last_name, country, age)

# 14. Check Python reserved keywords
help('keywords')
