# **Lab 3: Python Control Structures (if-else, loops, break/continue)**

## Create directory structure

```bash
mkdir -p ~/python/lab03/
```

# Change to lab03 directory

```bash
cd ~/python/lab03/
```

# Create control\_structures.py

```bash
cat >> control_structures.py << EOF
# If-Else Example
num = 15
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# For Loop Example
print("For loop 0-4:")
for i in range(5):
    print(i)

# While Loop Example
print("While loop 0-4:")
count = 0
while count < 5:
    print(count)
    count += 1

# Break Example
print("Break example:")
for i in range(5):
    if i == 3:
        break
    print(i)

# Continue Example
print("Continue example:")
for i in range(5):
    if i == 3:
        continue
    print(i)
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
python control_structures.py
```

**Expected Output:**

```
15 is odd
For loop 0-4:
0
1
2
3
4
While loop 0-4:
0
1
2
3
4
Break example:
0
1
2
Continue example:
0
1
2
4
```
