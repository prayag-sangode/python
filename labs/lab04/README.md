# **Lab 4: Python Functions**

## Create directory structure

```bash
mkdir -p ~/python/lab04/
```

# Change to lab04 directory

```bash
cd ~/python/lab04/
```

# Create functions.py

```bash
cat >> functions.py << EOF
# Function without arguments
def greet():
    print("Hello from function!")

greet()

# Function with arguments
def add(a, b):
    return a + b

result = add(10, 20)
print("Addition result:", result)

# Function with default arguments
def greet_name(name="Python"):
    print("Hello", name)

greet_name()
greet_name("Lab Student")

# Function returning multiple values
def arithmetic_ops(x, y):
    return x+y, x*y, x-y

sum_val, mul_val, sub_val = arithmetic_ops(5, 3)
print("Sum:", sum_val)
print("Product:", mul_val)
print("Difference:", sub_val)
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
python functions.py
```

**Expected Output:**

```
Hello from function!
Addition result: 30
Hello Python
Hello Lab Student
Sum: 8
Product: 15
Difference: 2
```
