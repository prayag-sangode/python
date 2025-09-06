# Lab 11: Inheritance & Polymorphism

## Create directory structure

```bash
mkdir -p ~/python/labs/lab11
```

## Change to lab11 directory

```bash
cd ~/python/labs/lab11
```

## Create inheritance\_polymorphism.py

```bash
cat >> inheritance_polymorphism.py << EOF
# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

# Child class Dog (inherits from Animal)
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Child class Cat (inherits from Animal)
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphism in action
animals = [Dog("Buddy"), Cat("Kitty"), Animal("Generic")]

for animal in animals:
    print(f"{animal.name} says: {animal.speak()}")
EOF
```

## Run in venv

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Create requirements.txt if required and run it

(No external requirements needed)

## Run the Python script

```bash
python inheritance_polymorphism.py
```

**Expected Output:**

```
Buddy says: Woof!
Kitty says: Meow!
Generic says: Some generic sound
```
