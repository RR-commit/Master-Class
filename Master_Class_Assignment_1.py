#Master Class Assignment 1

#Functional Programming

print("\n--- Lambda Example ---")
# 1. Lambda
square = lambda x: x * x
print(square(4))

print("\n--- Map Example ---")
# 2. Map
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print(squares)

print("\n--- Filter Example ---")
# 3. Filter
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

print("\n--- Reduce Example ---")
# 4. Reduce
from functools import reduce

numbers = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, numbers)
print(total)


#Pythonic Comprehensions

print("\n--- List Comprehension ---")
# 1. List
squares = [x*x for x in range(1, 6)]
print(squares) 

print("\n--- Dict Comprehension ---")
# 2. Dict
squares_dict = {x: x*x for x in range(1, 6)}
print(squares_dict) 

print("\n--- Nested List Comprehension ---")
# 3. Nested
table = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(table) 


#Backend Data Transformations

print("\n--- Sorting ---")
# 1. Sorting
numbers = [5, 2, 9, 1, 7]

# Sort in ascending order
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# Sort in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)

print("\n--- Grouping ---")
# 2. Grouping
from itertools import groupby

data = [("fruit", "apple"), ("fruit", "banana"),
        ("vegetable", "carrot"), ("fruit", "orange"),
        ("vegetable", "spinach")]

# First sort by the key to use groupby
data.sort(key=lambda x: x[0])

# Group by the first element
grouped = {k: [item[1] for item in g] for k, g in groupby(data, key=lambda x: x[0])}
print(grouped)

print("\n--- Pipelines ---")
# 3. Pipelines
numbers = [5, 2, 9, 1, 7]

# Pipeline: filter even numbers, square them, sort
result = sorted(map(lambda x: x*x, filter(lambda x: x % 2 == 0, numbers)))
print(result)

#File I/O basics

print("\n--- Text File I/O ---")
# 1. Text

# Write to a file
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("Python File I/O is easy!\n") 
    
# Read a file
with open("example.txt", "r") as file:
    content = file.read()
print(content)


print("\n--- JSON File I/O ---")
# 2. Json

# Write to a JSON
import json

data = {"name": "Alice", "age": 25, "skills": ["Python", "SQL"]}

with open("data.json", "w") as file:
    json.dump(data, file)

# Read a JSON
with open("data.json", "r") as file:
    data_loaded = json.load(file)
print(data_loaded)


print("\n--- CSV File I/O ---")
# 3. CSV

# Write to a CSV
import csv

data = [["Name", "Age"], ["Alice", 25], ["Bob", 20]]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Read a CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
