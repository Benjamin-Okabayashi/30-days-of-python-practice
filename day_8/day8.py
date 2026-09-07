# Create an empty dictionary called dog
dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name' : 'Hiro',
    'color': 'Brown',
    'breed': "golden doodle",
    'legs': "4",
    'Age': '7'
}
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "John", 
    "last_name": "Smith", 
    "gender": "Male", 
    "age": "23", 
    "marital status": "Single", 
    "skills": ["Coding", "Math", "tutoring"], 
    "country": "United States",
    "city": "Vancouver",
    "address": "1234 56th ave SW"
    }

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student["skills"])
print(type(student["skills"]))

# Modify the skills values by adding one or two skills
student['skills'].append('R')
student['skills'].append('Excel')
print(student['skills'])

# Get the dictionary keys as a list
student_keys = student.keys()
print(student_keys)

# Get the dictionary values as a list
student_values = student.values()
print(student_values)

# Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print(student_items)

# Delete one of the items in the dictionary
del student["first_name"]
print(student)

# Delete one of the dictionaries
del student
