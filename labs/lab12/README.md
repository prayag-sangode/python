# Lab 12: Decorators & Lambda Functions

## Create directory structure

```bash
mkdir -p ~/python/labs/lab12
```

## Change to lab12 directory

```bash
cd ~/python/labs/lab12
```

## Create decorators\_lambda.py

```bash
cat >> decorators_lambda.py << EOF
from functools import reduce

# --- Lambda Functions ---
square = lambda x: x * x
add = lambda a, b: a + b

print("Square of 5:", square(5))
print("Sum of 3 and 7:", add(3, 7))

# --- map(), filter(), reduce() ---
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x*x, numbers))
print("Squares:", squares)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)

product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)

# --- Custom Decorators ---
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

@log_decorator
def multiply(a, b):
    return a * b

@log_decorator
def greet(name):
    return f"Hello, {name}!"

# Using decorated functions
multiply(4, 5)
greet("Alice")
EOF
```

## Run in venv

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Create requirements.txt if required and run it

(No external requirements here)

## Run the Python script

```bash
python decorators_lambda.py
```

**Expected Output:**

```
Square of 5: 25
Sum of 3 and 7: 10
Squares: [1, 4, 9, 16, 25]
Evens: [2, 4]
Product of all numbers: 120
Calling function 'multiply' with arguments (4, 5)
Function 'multiply' returned 20
Calling function 'greet' with arguments ('Alice',)
Function 'greet' returned Hello, Alice!
```
