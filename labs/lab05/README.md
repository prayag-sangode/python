# **Lab 5: Lists, Tuples, Sets, Dictionaries**

## Create directory structure

```bash
mkdir -p ~/python/lab05/
```

# Change to lab05 directory

```bash
cd ~/python/lab05/
```

# Create data\_structures.py

```bash
cat >> data_structures.py << EOF
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
EOF
```

# Run in venv

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Create requirements.txt if required and install

```bash
# No additional requirements for this lab
touch requirements.txt
pip install -r requirements.txt
```

# Run the Python script

```bash
python data_structures.py
```

**Expected Output:**

```
Original list: ['apple', 'banana', 'cherry']
After append: ['apple', 'banana', 'cherry', 'orange']
After update: ['apple', 'blueberry', 'cherry', 'orange']
After remove: ['apple', 'blueberry', 'orange']
Access element: apple
Iterating list:
apple
blueberry
orange
Tuple: ('red', 'green', 'blue')
Access tuple element: green
Set: {1, 2, 3}
After add: {1, 2, 3, 4}
After discard: {1, 3, 4}
Iterating set:
1
3
4
Original dict: {'name': 'Alice', 'age': 25}
Updated dict: {'name': 'Alice', 'age': 26, 'city': 'Delhi'}
After delete: {'age': 26, 'city': 'Delhi'}
Iterating dictionary:
age : 26
city : Delhi
```

