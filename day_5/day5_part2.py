# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)
min_age = ages[0]
max_age =ages[-1]
print(min_age)
print(max_age)

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
ages.sort()
print(ages)
# Find the median age (one middle item or two middle items divided by two)
print(len(ages))
print(ages[6])
# Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
print(average_age)

# Find the range of the ages (max minus min)
range_age = max_age- min_age
print(range_age)
# Compare the value of (min - average) and (max - average), use abs() method
diff_min = abs(min_age - average_age)
diff_max = abs(max_age - average_age)

print(diff_min)
print(diff_max)
print(diff_min == diff_max)

# Find the middle country(ies) in the countries list
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
n = len(countries)
if n % 2 == 0:
    middle = [countries[n // 2 - 1], countries[n // 2]]
else:
    middle = countries[n // 2]
print(middle)
# Divide the countries list into two equal lists if it is even if not one more country for the first half.

mid_point = (n + 1) // 2
first_half = countries[:mid_point]
second_half = countries[mid_point:]
print(first_half)
print(second_half)

# Unpack the first three countries and the rest as scandic countries.
# Unpack first three, rest as scandic countries
first, second, third, *scandic_countries = countries
print(first, second, third)
print(scandic_countries)