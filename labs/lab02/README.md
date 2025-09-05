# **Lab 2: Python Variables & Data Types**

## Create directory structure

```bash
mkdir -p ~/python/lab02/
```

# Change to lab02 directory

```bash
cd ~/python/lab02/
```

# Create variables.py

```bash
cat >> variables.py << EOF
# Integer
num = 10
print("Integer:", num)

# Float
pi = 3.1415
print("Float:", pi)

# String
name = "Python Lab"
print("String:", name)

# Boolean
flag = True
print("Boolean:", flag)
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
python variables.py
```

**Expected Output:**

```
Integer: 10
Float: 3.1415
String: Python Lab
Boolean: True
```

