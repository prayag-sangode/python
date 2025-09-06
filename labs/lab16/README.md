# Lab 16: SQLAlchemy ORM Basics (Python + SQLite)

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab16
cd ~/python/labs/lab16
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
sqlalchemy
EOF
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Step 3: Create `sqlalchemy_orm.py`

```bash
cat >> sqlalchemy_orm.py << EOF
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Define base class
Base = declarative_base()

# Define Employee model
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    dept = Column(String, nullable=False)

    def __repr__(self):
        return f"<Employee(id={self.id}, name='{self.name}', age={self.age}, dept='{self.dept}')>"

def main():
    # Create SQLite database
    engine = create_engine("sqlite:///company.db", echo=True)

    # Create tables
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clean table for repeatable runs
    session.query(Employee).delete()
    session.commit()

    # Insert employees
    emp1 = Employee(name="Alice", age=30, dept="HR")
    emp2 = Employee(name="Bob", age=25, dept="IT")
    session.add_all([emp1, emp2])
    session.commit()
    print("Inserted employees")

    # Query employees
    print("Employees:")
    for emp in session.query(Employee).all():
        print(emp)

    # Update employee
    alice = session.query(Employee).filter_by(name="Alice").first()
    alice.age = 31
    session.commit()
    print("Updated Alice's age")

    # Delete employee
    bob = session.query(Employee).filter_by(name="Bob").first()
    session.delete(bob)
    session.commit()
    print("Deleted Bob")

    # Final list
    print("Final Employees:")
    for emp in session.query(Employee).all():
        print(emp)

    session.close()

if __name__ == "__main__":
    main()
EOF
```

---

## Step 4: Run the Script

```bash
python sqlalchemy_orm.py
```

---

## ✅ Expected Output

(SQLAlchemy prints SQL statements because `echo=True`)

```
Inserted employees
Employees:
<Employee(id=1, name='Alice', age=30, dept='HR')>
<Employee(id=2, name='Bob', age=25, dept='IT')>
Updated Alice's age
Deleted Bob
Final Employees:
<Employee(id=1, name='Alice', age=31, dept='HR')>
```
