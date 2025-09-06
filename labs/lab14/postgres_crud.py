import psycopg2

# Database connection details
DB_HOST = "localhost"
DB_NAME = "testdb"
DB_USER = "testuser"
DB_PASS = "password"

# Connect to PostgreSQL
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
    if cursor:
        cursor.close()
    if conn:
        conn.close()
        print("Connection closed")
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
