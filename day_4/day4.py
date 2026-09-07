# 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
t = 'Thirty '
d =  'Days '
o = 'Of '
p = 'Python'
space = ' '

first_s = t + d + o + p 
print(first_s)
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
coding = 'coding '
For = 'for '
All = 'all'
code_for = coding + For + All
print(code_for)
# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().
company = "Coding For All"
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
company_1 = company.upper()
print(company_1)
# Change all the characters to lowercase letters using lower() method.
company_2 = company.lower()
print(company_2)

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
company = "Coding For All"
first_word = company[0:6]
print(first_word)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding"))

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
p_for_e = "Python For Everyone"
print(p_for_e.replace("Everyone", "All"))

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
many_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(many_companies.split(", "))

# What is the character at index 0 in the string Coding For All.
print(company[0])
# What is the last index of the string Coding For All.
print(company[-1])
# What character is at index 10 in "Coding For All" string.
print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym2 = ''.join([word[0] for word in p_for_e.split()])
print(acronym2)
# Create an acronym or an abbreviation for the name 'Coding For All'.
acronym2 = ''.join([word[0] for word in company.split()])
print(acronym2)

# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.lower().find('c'))

# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.lower().find('f'))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
people = "Coding For All People"
print(people.lower().rfind("l"))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
new_s = 'You cannot end a sentence with because because because is a conjunction'
print(new_s.lower().find('because'))
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new_s.lower().rfind('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new_s[31:54])
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Does 'Coding For All' start with a substring Coding?
# Does 'Coding For All' end with a substring coding?
print(company.startswith('Coding'))
print(company.endswith('coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
new_code = '   Coding For All      '  
print(new_code[3:17])

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
thirty= '30DaysOfPython'
second_thirty= 'thirty_days_of_python'
print(thirty.isidentifier())
print(second_thirty.isidentifier())
#the second one because doesn't have number at start


# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

stuff =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(stuff)
print(result)

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print( "I am enjoying this challenge. \nI just wonder what is next.")

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print(" Name\t Age \tCountry \tCity \nAsabeneh \t250 \tFinland \tHelsinki")

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")
# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a=8
b=6

print(f"{a}+{b} = {a+b}")
print(f"{a}-{b} = {a-b}")
print(f"{a}*{b} = {a*b}")
print(f"{a}/{b} = {a/b}")
print(f"{a}%{b} = {a%b}")
print(f"{a}//{b}= {a//b}")
print(f"{a}**{b} = {a**b}")