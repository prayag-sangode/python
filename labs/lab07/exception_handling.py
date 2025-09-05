# Example 1: Simple try-except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Example 2: Multiple exceptions
try:
    num = int("abc")  # This will raise ValueError
except ValueError:
    print("Error: Invalid conversion to integer.")
except TypeError:
    print("Error: Wrong data type used.")

# Example 3: try-except-finally
try:
    f = open("non_existing_file.txt", "r")
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("This block always runs, cleaning up resources if needed.")

# Example 4: Catch all exceptions (not recommended in real apps)
try:
    result = 10 / "five"
except Exception as e:
    print("Caught an exception:", e)
