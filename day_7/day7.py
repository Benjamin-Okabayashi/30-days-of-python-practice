# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# Exercises: Level 1
# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(["Hiya", "NVIDIA"])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove("Hiya")
print(it_companies)

# What is the difference between remove and discard
## if the item does not exist in the set then remove will cause errors whereas discard wouldn't


# Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# Join A and B
C = A.union(B)
print(C)
# Find A intersection B
D = A.intersection(B)
print(D)

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
A.update(B)
B.update(A)

print(A, B)

# What is the symmetric difference between A and B
## B has 27 and 28 in its set 

# Delete the sets completely
del A
del B


# Exercises: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set_age = set(age)
print(len(age), len(set_age))
# the list is 8 and the set is 5 so the list is bigger

# Explain the difference between the following data types: string, list, tuple and set
# a string is String (str) — an ordered sequence of characters (text), written in quotes: "hello". Immutable — once created, 
# you can't change individual characters in place; any "modification" (like .upper()) actually creates a new string.

# List (list) — an ordered, mutable collection of items, written with []: [1, 2, 3]. 
# You can add, remove, or change items after creation (.append(), .insert(), reassigning by index). 
# Items can repeat, and order is preserved — index 0 will always be the item you put first.

# Tuple (tuple) — an ordered, immutable collection, written with (): (1, 2, 3). 
# Looks similar to a list, but once created, you can't add, remove, or change items. 
# Order is preserved, and duplicates are allowed, just like lists. 
# You'd use a tuple over a list when you want to guarantee the data can't accidentally get changed later.

# Set (set) — an unordered collection of unique items, written with {}: {1, 2, 3}. 
# Duplicates are automatically removed, and since there's no order, you can't access items by index (my_set[0] doesn't work). 
# Sets are useful specifically for membership checks (x in my_set is very fast) and removing duplicates from data.

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."

base_words = sentence.split()
print(base_words)

unique_words = set(base_words)
print(unique_words)

print(len(unique_words))