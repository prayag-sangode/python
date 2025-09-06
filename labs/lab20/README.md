# Lab 20: Flask Request & Response

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab20
cd ~/python/labs/lab20
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
from flask import Flask, request, jsonify

app = Flask(__name__)

# GET request with query parameters
@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "Guest")
    return jsonify({"message": f"Hello, {name}!"})

# POST request with JSON body
@app.route("/sum", methods=["POST"])
def sum_numbers():
    data = request.get_json()
    if not data or "a" not in data or "b" not in data:
        return jsonify({"error": "Please provide 'a' and 'b' in JSON body"}), 400
    result = data["a"] + data["b"]
    return jsonify({"a": data["a"], "b": data["b"], "sum": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
EOF
```

---

## Step 4: Run the Flask App

```bash
python app.py
```

* Server runs at **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## Step 5: Test Endpoints

### 1️⃣ GET `/greet` with query parameter

```bash
curl "http://127.0.0.1:5000/greet?name=Alice"
```

**Expected Output:**

```json
{"message": "Hello, Alice!"}
```

If no name provided:

```bash
curl "http://127.0.0.1:5000/greet"
```

```json
{"message": "Hello, Guest!"}
```

---

### 2️⃣ POST `/sum` with JSON body

```bash
curl -X POST "http://127.0.0.1:5000/sum" -H "Content-Type: application/json" -d '{"a":5,"b":10}'
```

**Expected Output:**

```json
{"a": 5, "b": 10, "sum": 15}
```

If JSON is invalid or missing keys:

```bash
curl -X POST "http://127.0.0.1:5000/sum" -H "Content-Type: application/json" -d '{}'
```

```json
{"error": "Please provide 'a' and 'b' in JSON body"}
```

---

### Key Learning Points

* Access **query parameters** using `request.args.get()`
* Access **JSON request body** using `request.get_json()`
* Return **JSON responses** using `jsonify()`
* Handle **error responses** with proper status codes

