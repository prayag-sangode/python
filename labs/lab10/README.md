# Lab 10: Classes & Objects

## Create directory structure

```bash
mkdir -p ~/python/labs/lab10
```

## Change to lab10 directory

```bash
cd ~/python/labs/lab10
```

## Create classes\_objects.py

```bash
cat >> classes_objects.py << EOF
# Define a simple class
class Car:
    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Method to display car info
    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Create objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model 3")

# Access object attributes
print("Car 1 brand:", car1.brand)
print("Car 2 model:", car2.model)

# Call methods
car1.display_info()
car2.display_info()
EOF
```

## Run in venv

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Create requirements.txt if required and run it

(No external requirements for this lab)

## Run the Python script

```bash
python classes_objects.py
```

**Expected Output:**

```
Car 1 brand: Toyota
Car 2 model: Model 3
Car: Toyota Corolla
Car: Tesla Model 3
```
