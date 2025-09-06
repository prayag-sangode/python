# Lab 17: SQLAlchemy Relationships (One-to-Many & Many-to-Many)

## 1. Create Project Directory

```bash
mkdir -p ~/python/labs/lab17
cd ~/python/labs/lab17
```

---

## 2. Setup Virtual Environment

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

## 3. Create `sqlalchemy_relationships.py`

```bash
cat >> sqlalchemy_relationships.py << EOF
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# Many-to-Many association table
employee_project = Table(
    "employee_project",
    Base.metadata,
    Column("employee_id", Integer, ForeignKey("employees.id"), primary_key=True),
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True)
)

# One-to-Many: Department -> Employees
class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    employees = relationship("Employee", back_populates="department")

    def __repr__(self):
        return f"<Department(id={self.id}, name='{self.name}')>"

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    dept_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="employees")
    projects = relationship("Project", secondary=employee_project, back_populates="employees")

    def __repr__(self):
        return f"<Employee(id={self.id}, name='{self.name}', dept_id={self.dept_id})>"

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    employees = relationship("Employee", secondary=employee_project, back_populates="projects")

    def __repr__(self):
        return f"<Project(id={self.id}, title='{self.title}')>"

def main():
    engine = create_engine("sqlite:///company_rel.db", echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clean tables
    session.query(Employee).delete()
    session.query(Project).delete()
    session.query(Department).delete()
    session.commit()

    # One-to-Many
    hr = Department(name="HR")
    it = Department(name="IT")
    alice = Employee(name="Alice", department=hr)
    bob = Employee(name="Bob", department=it)
    charlie = Employee(name="Charlie", department=it)
    session.add_all([hr, it, alice, bob, charlie])
    session.commit()

    print("\\nDepartments and Employees:")
    for dept in session.query(Department).all():
        print(dept, "->", dept.employees)

    # Many-to-Many
    proj1 = Project(title="Website Revamp")
    proj2 = Project(title="AI Research")
    alice.projects.append(proj1)
    bob.projects.append(proj1)
    bob.projects.append(proj2)
    charlie.projects.append(proj2)
    session.commit()

    print("\\nProjects and Employees:")
    for proj in session.query(Project).all():
        print(proj, "->", proj.employees)

    session.close()

if __name__ == "__main__":
    main()
EOF
```

---

## 4. Run the Script

```bash
python sqlalchemy_relationships.py
```

---

### ✅ Expected Output

```
Departments and Employees:
<Department(id=1, name='HR')> -> [<Employee(id=1, name='Alice', dept_id=1)>]
<Department(id=2, name='IT')> -> [<Employee(id=2, name='Bob', dept_id=2)>, <Employee(id=3, name='Charlie', dept_id=2)>]

Projects and Employees:
<Project(id=1, title='Website Revamp')> -> [<Employee(id=1, name='Alice', dept_id=1)>, <Employee(id=2, name='Bob', dept_id=2)>]
<Project(id=2, title='AI Research')> -> [<Employee(id=2, name='Bob', dept_id=2)>, <Employee(id=3, name='Charlie', dept_id=2)>]
```
