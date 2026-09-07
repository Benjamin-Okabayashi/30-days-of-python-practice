# # Declare your age as integer variable
# # Declare your height as a float variable
# # Declare a variable that store a complex number
# # Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# #     Enter base: 20
# #     Enter height: 10
# #     The area of the triangle is 100
# # Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# # Enter side a: 5
# # Enter side b: 4
# # Enter side c: 3
# # The perimeter of the triangle is 12
# # Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# # Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# # Calculate the slope, x-intercept and y-intercept of y = 2x -2
# # Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# # Compare the slopes in tasks 8 and 9.
# # Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# # Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# # Use and operator to check if 'on' is found in both 'python' and 'dragon'
# # I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# # There is no 'on' in both dragon and python
# # Find the length of the text python and convert the value to float and convert it to string
# # Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# # Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# # Check if type of '10' is equal to type of 10
# # Check if int('9.8') is equal to 10
# # Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# # Enter hours: 40
# # Enter rate per hour: 28
# # Your weekly earning is 1120
# # # Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# # # Enter number of years you have lived: 100
# # # You have lived for 3153600000 seconds.
# # # Write a Python script that displays the following table

# #1 Declare your age as integer variable

# age= 23
# #2 Declare your height as a float variable
# height = 6.2
# print(type(age))     # <class 'int'>
# print(type(height))  # <class 'float'>

# #3 Declare a variable that store a complex number
# comp_number = 1 + 1j
# complex_num = 3 + 4j

# # 4 Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# #     Enter base: 20
# #     Enter height: 10
# #     The area of the triangle is 100

# base  = float(input("Enter base: "))
# height = float(input("Enter height: "))
# area = base * height * 0.5
# print("The area of the triangle is ", base)

# # 5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# # Enter side a: 5
# # Enter side b: 4
# # Enter side c: 3
# # The perimeter of the triangle is 12

# side_a = float(input("Enter side a: "))
# side_b = float(input("Enter side b: "))
# side_c = float(input("Enter side c: "))
# perimeter = side_a + side_b + side_c
# print ("The perimeter of the triangle is ",perimeter )


# # 6 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
# rec_area = width * length 
# perimeter = 2 * (width+ length)
# print( "This is the area: ", rec_area)
# print( "This is the perimeter: ", perimeter)
# # 7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

# radius = float(input("Enter radius: "))
# circumference = 2* 3.14 * radius
# print( " The circumference is ", circumference)
# 8 Calculate the slope, x-intercept and y-intercept of y = 2x -2


# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python_len = len('python')
dragon_len = len('dragon')
print( dragon_len != python_len)


# Use and operator to check if 'on' is found in both 'python' and 'dragon'

on_in_python = 'on' in 'python'
on_in_dragon = 'on' in 'dragon'
print( on_in_dragon and on_in_python)
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
jargon_check = 'jargon' in 'I hope this course is not full of jargon.'
print(jargon_check )
# There is no 'on' in both dragon and python

# Find the length of the text python and convert the value to float and convert it to string
len_python = float(len('python'))
print(type(len_python))
str_python = str(len_python)
print(type(str_python))


# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
is_even = float(input("check if your number is even: "))
check_even = (is_even%2 ==0)
print(check_even)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7))

# Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# Check if int('9.8') is equal to 10
print(int(9.8)== 10)
# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("How many hours do you work"))
wage = float(input("Whats your wage"))
salary = wage*hours
print(salary)

# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
# Write a Python script that displays the following table
for n in range(1, 6):
    print(n, n**0, n**1, n**2, n**3)
    



