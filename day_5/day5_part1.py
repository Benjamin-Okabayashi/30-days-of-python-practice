# Declare an empty list
new_list = []
# could also do 
# new_list = list()

# Declare a list with more than 5 items
sec_list = ["adidas", "reebok", "doc martin", "nikes", "new balance"]

# Find the length of your list
print(len(sec_list))
# Get the first item, the middle item and the last item of the list
print(sec_list[0], sec_list[2], sec_list[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Benjamin", 23, 186, "single", "nope"]
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])
# Print the list after modifying one of the companies
it_companies[0] = "Meta"
print(it_companies)
# Add an IT company to it_companies
it_companies.append("NVIDIA")
# Insert an IT company in the middle of the companies list
it_companies.insert(3,"SpaceX")

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3]= it_companies[3].upper()
print(it_companies)
# Join the it_companies with a string '#;  '

new_string = "#:  ".join(it_companies)
print(new_string)

# Check if a certain company exists in the it_companies list.
print('Google' in it_companies)
# Sort the list using sort() method
print('5')
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)
# Slice out the first 3 companies from the list
first_3 = it_companies[0:3]
print(first_3)
# Slice out the last 3 companies from the list
last_3 = it_companies[-4:-1]
print(last_3)
# Slice out the middle IT company or companies from the list
print(len(it_companies)/2)
middle = it_companies[4:5]
print(middle)
# Remove the first IT company from the list
print(it_companies)
it_companies.pop(0)
print(it_companies)
# Remove the middle IT company or companies from the list
it_companies.pop(4)
print(it_companies)
# Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)
# Remove all IT companies from the list
it_companies.clear()
print(it_companies)
# Destroy the IT companies list
del it_companies
# Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
both_end = front_end + back_end
print(both_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack
full_stack = both_end.copy()
print(full_stack)
# then insert Python and SQL after Redux.
redux_position = full_stack.index('Redux')
full_stack.insert(redux_position+1, "SQL")
full_stack.insert(redux_position+2, "Python")
print(full_stack)

