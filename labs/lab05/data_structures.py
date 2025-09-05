# LISTS
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# CRUD Operations
fruits.append("orange")          # Create / Add
print("After append:", fruits)
fruits[1] = "blueberry"          # Update
print("After update:", fruits)
fruits.remove("cherry")          # Delete
print("After remove:", fruits)
print("Access element:", fruits[0]) # Read / Access

# Iteration
print("Iterating list:")
for fruit in fruits:
    print(fruit)

# TUPLES
colors = ("red", "green", "blue")
print("Tuple:", colors)
print("Access tuple element:", colors[1])

# SETS
numbers = {1, 2, 3, 3, 2}  # duplicates removed automatically
print("Set:", numbers)
numbers.add(4)              # Add
print("After add:", numbers)
numbers.discard(2)          # Remove
print("After discard:", numbers)

# Iteration
print("Iterating set:")
for num in numbers:
    print(num)

# DICTIONARIES
person = {"name": "Alice", "age": 25}
print("Original dict:", person)
person["age"] = 26          # Update
person["city"] = "Delhi"    # Add
print("Updated dict:", person)
del person["name"]          # Delete
print("After delete:", person)

# Iteration
print("Iterating dictionary:")
for key, value in person.items():
    print(key, ":", value)
