# **Lab 7: Python Exception Handling**

## Create directory structure

```bash
mkdir -p ~/python/lab07/
```

# Change to lab07 directory

```bash
cd ~/python/lab07/
```

# Create exception\_handling.py

```bash
cat >> exception_handling.py << EOF
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
python exception_handling.py
```

**Expected Output:**

```
Error: Division by zero is not allowed.
Error: Invalid conversion to integer.
Error: File not found.
This block always runs, cleaning up resources if needed.
Caught an exception: unsupported operand type(s) for /: 'int' and 'str'
```
