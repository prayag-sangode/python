# **Lab 8: Python Modules & Packages**

## Create directory structure

```bash
mkdir -p ~/python/labs/lab08/mypackage
```

# Change to lab08 directory

```bash
cd ~/python/labs/lab08/
```

# Create a module file inside the package

```bash
cat >> mypackage/mymodule.py << EOF
def greet(name):
    return f"Hello, {name} from mymodule!"
EOF
```

# Create another module using standard library (`os`, `sys`)

```bash
cat >> mypackage/sysinfo.py << EOF
import os
import sys

def show_info():
    print("Current Working Directory:", os.getcwd())
    print("Python Executable Path:", sys.executable)
    print("Command Line Arguments:", sys.argv)
EOF
```

# Create main script to import modules

```bash
cat >> main.py << EOF
from mypackage import mymodule, sysinfo

# Use custom module
print(mymodule.greet("Developer"))

# Use sysinfo module
sysinfo.show_info()
EOF
```

# Run in venv

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Create requirements.txt if required and install

```bash
# No external dependencies required
touch requirements.txt
pip install -r requirements.txt
```

# Run the Python script

```bash
python main.py
```

**Expected Output:**

```
Hello, Developer from mymodule!
Current Working Directory: /home/username/python/labs/lab08
Python Executable Path: /home/username/python/labs/lab08/myenv/bin/python
Command Line Arguments: ['main.py']
```
