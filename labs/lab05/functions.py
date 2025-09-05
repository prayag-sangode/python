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
