# Lab 18: Flask Hello World

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab18
cd ~/python/labs/lab18
```

---

## Step 2: Setup Virtual Environment

```bash
python3 -m venv myenv
source myenv/bin/activate
```

Create **requirements.txt**:

```bash
cat >> requirements.txt << EOF
flask
EOF
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Step 3: Create Flask App `app.py`

```bash
cat >> app.py << EOF
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
EOF
```

---

## Step 4: Run the Flask App

```bash
python app.py
```

* The server will start on **[http://0.0.0.0:5000/](http://0.0.0.0:5000/)**
* Open a browser or use `curl` to test:

```bash
curl http://127.0.0.1:5000/
```

---

### ✅ Expected Output

```
Hello, World!
```

* Flask will also show logs in the terminal: requests, debug info, etc.
