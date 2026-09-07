# Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. Output:

age = float(input('Enter your age: '))
if age>18:
    print("You are old enough to drive")
else: 
    age_missing = 18-age
    print("You are ",age_missing, " years away from being able to drive" )


my_age = 24 
your_age = float(input('Enter your age: '))
if your_age>my_age:
    if your_age-1==my_age:
        print("You are one year older than me")
    else:
        print("You are " , your_age-my_age, "years older than me.")    
elif your_age<my_age:
    if my_age-1==your_age:
        print("I am one year older than you")
    else: 
        print("I am ", my_age-your_age, " years older than you.")    
else: 
    print("We are the same age!")

# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, 
# else a is equal to b

A = int(input("Pick first number: "))
B = int(input("Pick second number: "))
if A>B:
    print(A, " is greater than ", B)
elif A<B:
    print(B, " is greater than " ,A)
else:
    print("Both ", A ," and ", B ," are the same value")

#     Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
# 90-100, A.  80-89, B.  70-79, C.  60-69, D.  0-59, F
student_grade = float(input("What did you score? "))

if 100>student_grade>=90:
    print("You got an A")
elif 90>student_grade>=80:
    print("You got a B")
elif 80>student_grade>=70:
    print("You got a C")
elif 70>student_grade>=60:
    print("You got a D")
else: 
    print("You got a F")

# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer
season = input("Enter a month to see what season it is. ")
if season== "September" or season == "October" or season =="November":
    print("The season is Autumn")
elif season== "December" or season == "January" or season =="February":
    print("The season is Winter")
elif season== "March" or season == "April" or season =="May":
    print("The season is Spring")
else:
    print("The season is summer")


# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = input("What fruit are you looking for? ")
if new_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(new_fruit)
    print(fruits)




# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person:
    skills = person["skills"]
    middle_skill = len(skills)//2
    print(skills[middle_skill])
else: 
    print("there is no skills key")

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person: 
    skills = person["skills"]
    print("Python" in skills)
else:
    print("there is no skills key")

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), 
#       if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
#       if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
#       else print('unknown title') - for more accurate results more conditions can be nested!

if "skills" in person:
    skills = person["skills"]
    if set(skills) == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
    else:
        print('unknown title')


#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.

if "country" in person and "is_married" in person:
    if True == person["is_married"]:
        print(person["first_name"], person["last_name"], "lives in ", person["country"],". He is married")


