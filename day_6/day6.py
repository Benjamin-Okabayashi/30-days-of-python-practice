# Create an empty tuple
new_tuple = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("John", "Alex", "Mark")
sisters = ("Mary", "Sophia")

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ("Bob", "Josie")
print(family_members)

# Unpack siblings and parents from family_members
*siblings_only, father, mother = family_members
print(siblings)
parents = father+ " "+ mother
print(parents)


# Create fruits, vegetables and animal products tuples. 
fruit = ("apple", "orange")
vegatables = ("lettuce", "cucumber")
animal = ("chicken", "beef")

# Join the three tuples and assign it to a variable called food_stuff_tp.
food_stuff_tp = fruit + vegatables + animal

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_tp = food_stuff_tp[2:4]
print(middle_tp)

# Slice out the first three items and the last three items from food_stuff_lt list
first_food_lt = food_stuff_lt[0:3]
last_food_lt = food_stuff_lt[3:]
print(first_food_lt)
print(last_food_lt)

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)
