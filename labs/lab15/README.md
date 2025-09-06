Perfect 👌 — MongoDB **8.0** now has **official support for Ubuntu 24.04 (Noble)** 🎉 so let’s update your lab with this installation flow + Python CRUD code.

Here’s the **updated `README.md` for MongoDB CRUD (Lab 15)**:

---

# Lab 15: MongoDB CRUD with Python

In this lab, you will:

1. Install MongoDB Community Edition on Ubuntu 24.04 (Noble).
2. Connect to MongoDB using Python (`pymongo`).
3. Perform CRUD operations (Create, Read, Update, Delete).

---

## Step 1: Install MongoDB on Ubuntu 24.04

### Import the MongoDB GPG key

```bash
sudo apt-get update
sudo apt-get install -y gnupg curl

curl -fsSL https://www.mongodb.org/static/pgp/server-8.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg \
   --dearmor
```

### Add the MongoDB repo for Noble (24.04)

```bash
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.0 multiverse" | \
sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list
```

### Update package list & install MongoDB

```bash
sudo apt-get update
sudo apt-get install -y mongodb-org
```

### Start & enable MongoDB service

```bash
sudo systemctl enable --now mongod
systemctl status mongod
```

---

## Step 2: Create Project Directory

```bash
mkdir -p ~/python/labs/lab15
cd ~/python/labs/lab15
```

---

## Step 3: Setup Virtual Environment

```bash
python3 -m venv myenv
source myenv/bin/activate
```

Create **requirements.txt**:

```bash
cat >> requirements.txt << EOF
pymongo
EOF
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Step 4: Create MongoDB CRUD Script

```bash
cat >> mongodb_crud.py << EOF
from pymongo import MongoClient

def main():
    # Connect to local MongoDB
    client = MongoClient("mongodb://localhost:27017/")

    # Create/use database
    db = client["company"]

    # Create/use collection
    employees = db["employees"]

    # Clean collection for repeatable runs
    employees.delete_many({})

    # Insert documents
    employees.insert_many([
        {"name": "Alice", "age": 30, "dept": "HR"},
        {"name": "Bob", "age": 25, "dept": "IT"}
    ])
    print("Inserted employees")

    # Read documents
    print("Employees:")
    for emp in employees.find():
        print(emp)

    # Update a document
    employees.update_one({"name": "Alice"}, {"$set": {"age": 31}})
    print("Updated Alice's age")

    # Delete a document
    employees.delete_one({"name": "Bob"})
    print("Deleted Bob")

    # Final list
    print("Final Employees:")
    for emp in employees.find():
        print(emp)

    client.close()

if __name__ == "__main__":
    main()
EOF
```

---

## Step 5: Run the Script

```bash
python mongodb_crud.py
```

---

### ✅ Expected Output

```
Inserted employees
Employees:
{'_id': ObjectId('...'), 'name': 'Alice', 'age': 30, 'dept': 'HR'}
{'_id': ObjectId('...'), 'name': 'Bob', 'age': 25, 'dept': 'IT'}
Updated Alice's age
Deleted Bob
Final Employees:
{'_id': ObjectId('...'), 'name': 'Alice', 'age': 31, 'dept': 'HR'}
```

---

Would you like me to also add a **cleanup section** (dropping the `company` DB at the end) so that you can re-run this lab multiple times without manually deleting docs?
