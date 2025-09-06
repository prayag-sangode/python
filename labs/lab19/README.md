# Lab 19: Flask Routes & Templates

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab19/templates
cd ~/python/labs/lab19
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
from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# About route
@app.route("/about")
def about():
    return render_template("about.html")

# Contact route
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
EOF
```

---

## Step 4: Create HTML Templates

### `templates/index.html`

```bash
cat >> templates/index.html << EOF
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Flask Home Page</h1>
    <a href="/about">About</a> | <a href="/contact">Contact</a>
</body>
</html>
EOF
```

### `templates/about.html`

```bash
cat >> templates/about.html << EOF
<!DOCTYPE html>
<html>
<head>
    <title>About</title>
</head>
<body>
    <h1>About Page</h1>
    <a href="/">Home</a> | <a href="/contact">Contact</a>
</body>
</html>
EOF
```

### `templates/contact.html`

```bash
cat >> templates/contact.html << EOF
<!DOCTYPE html>
<html>
<head>
    <title>Contact</title>
</head>
<body>
    <h1>Contact Page</h1>
    <a href="/">Home</a> | <a href="/about">About</a>
</body>
</html>
EOF
```

---

## Step 5: Run the Flask App

```bash
python app.py
```

* Open a browser and test:

  * Home: `http://127.0.0.1:5000/`
  * About: `http://127.0.0.1:5000/about`
  * Contact: `http://127.0.0.1:5000/contact`

---

### ✅ Expected Behavior

* Clicking links navigates between pages.
* Each page renders the correct HTML template.
* Flask debug logs appear in the terminal for each request.
