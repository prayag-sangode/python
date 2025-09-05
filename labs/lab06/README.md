# **Lab 6: Python File Handling (Text & JSON)**

## Create directory structure

```bash
mkdir -p ~/python/lab06/
```

# Change to lab06 directory

```bash
cd ~/python/lab06/
```

# Create file\_handling.py

```bash
cat >> file_handling.py << EOF
import json

# ----------- TEXT FILE HANDLING -----------
# Write to a text file
with open("sample.txt", "w") as f:
    f.write("Hello, this is a text file.\\n")
    f.write("This is another line.\\n")

# Read from a text file
with open("sample.txt", "r") as f:
    content = f.read()
    print("Text file content:")
    print(content)

# ----------- JSON FILE HANDLING -----------
data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Flask", "FastAPI"]
}

# Write JSON to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Read JSON from file
with open("data.json", "r") as f:
    loaded_data = json.load(f)
    print("JSON file content:")
    print(loaded_data)
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
python file_handling.py
```

**Expected Output:**

```
Text file content:
Hello, this is a text file.
This is another line.

JSON file content:
{'name': 'Alice', 'age': 25, 'skills': ['Python', 'Flask', 'FastAPI']}
```
