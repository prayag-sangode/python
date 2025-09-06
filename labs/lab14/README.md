# Lab 14: PostgreSQL CRUD with psycopg2 (Ubuntu 24)

This lab will install PostgreSQL, configure a database and user, grant schema privileges, and then perform CRUD operations using Python with **`psycopg2`**.

---

## 1. Install PostgreSQL on Ubuntu 24

```bash
sudo apt update
sudo apt install -y postgresql postgresql-contrib
```

---

## 2. Start & Enable PostgreSQL

```bash
sudo systemctl enable postgresql
sudo systemctl start postgresql
```

---

## 3. Set up Database, User, and Permissions

```bash
sudo -i -u postgres psql << EOF
-- Create database
CREATE DATABASE testdb;

-- Create user with password
CREATE USER testuser WITH ENCRYPTED PASSWORD 'password';

-- Grant privileges on database
GRANT ALL PRIVILEGES ON DATABASE testdb TO testuser;

\c testdb

-- Fix: allow testuser to use and create objects in schema
GRANT ALL ON SCHEMA public TO testuser;
ALTER SCHEMA public OWNER TO testuser;

\q
EOF
```

---

## 4. Create Project Directory

```bash
mkdir -p ~/python/labs/lab14
cd ~/python/labs/lab14
```

---

## 5. Create requirements.txt

```bash
cat >> requirements.txt << EOF
psycopg2-binary
EOF
```

---

## 6. Create postgres\_crud.py

```bash
cat >> postgres_crud.py << EOF
import psycopg2

# Database connection details
DB_HOST = "localhost"
DB_NAME = "testdb"
DB_USER = "testuser"
DB_PASS = "password"

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    cursor = conn.cursor()
    print("Connected to PostgreSQL")

    # Create table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        age INT,
        department VARCHAR(50)
    )
    """)
    conn.commit()

    # Insert data
    cursor.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)", 
                   ("Alice", 30, "HR"))
    cursor.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)", 
                   ("Bob", 25, "IT"))
    conn.commit()
    print("Data inserted")

    # Select data
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    print("Employees:")
    for row in rows:
        print(row)

    # Update data
    cursor.execute("UPDATE employees SET age = %s WHERE name = %s", (35, "Alice"))
    conn.commit()
    print("Data updated")

    # Delete data
    cursor.execute("DELETE FROM employees WHERE name = %s", ("Bob",))
    conn.commit()
    print("Data deleted")

except Exception as e:
    print("Error:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
        print("Connection closed")
EOF
```

---

## 7. Create & Activate Virtual Environment

```bash
python3 -m venv myenv
source myenv/bin/activate
```

---

## 8. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 9. Run the Script

```bash
python postgres_crud.py
```

---

### ✅ Expected Output

```
Connected to PostgreSQL
Data inserted
Employees:
(1, 'Alice', 30, 'HR')
(2, 'Bob', 25, 'IT')
Data updated
Data deleted
Connection closed
```
