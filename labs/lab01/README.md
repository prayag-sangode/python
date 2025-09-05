### Create project directory
### Clone exsiting repo
```bash
https://github.com/prayag-sangode/python
```

or

### Create directorry strucute
```bash
mkdir -p ~/python/lab01/
```

### Change to lab01 directory
```bash
cd ~/python/lab01/
```

### Create hello.py or use existing cloned one
```bash
cat >> hello.py << EOF
print("Hello World")
EOF
```

### Run in venv
```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Run the Python script
```bash
python hello.py
```

**Expected Output:**

```bash
Hello World
```
