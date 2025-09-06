# Lab 26: API Versioning in FastAPI (Updated)

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab26
cd ~/python/labs/lab26
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
fastapi
uvicorn
EOF
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Step 3: Create FastAPI App `main.py` (Updated)

```bash
cat >> main.py << EOF
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Versioned API Example")

# ------------------ Models ------------------ #
class User(BaseModel):
    id: int
    name: str
    email: str

class UserV2(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True

# ------------------ In-memory DB ------------------ #
users_db = []

# ------------------ Version 1 ------------------ #
@app.get("/v1/users", response_model=List[User])
def get_users_v1():
    return users_db

@app.post("/v1/users", response_model=User)
def create_user_v1(user: User):
    users_db.append(user)
    return user

# ------------------ Version 2 ------------------ #
@app.get("/v2/users", response_model=List[UserV2])
def get_users_v2():
    result = []
    for user in users_db:
        # Convert old User to dict with is_active=True
        if isinstance(user, User):
            result.append(UserV2(**user.dict(), is_active=True))
        else:
            # Already UserV2
            result.append(user)
    return result

@app.post("/v2/users", response_model=UserV2)
def create_user_v2(user: UserV2):
    users_db.append(user)
    return user
EOF
```

---

## Step 4: Run the FastAPI App

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

* Server: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**
* Interactive docs:

  * Swagger UI: `http://127.0.0.1:8000/docs`
  * Redoc: `http://127.0.0.1:8000/redoc`

---

## Step 5: Test Endpoints

### 1️⃣ Version 1: Create User

```bash
curl -X POST "http://127.0.0.1:8000/v1/users" \
-H "Content-Type: application/json" \
-d '{"id":1,"name":"Alice","email":"alice@example.com"}'
```

**Expected Output:**

```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com"
}
```

---

### 2️⃣ Version 1: Get Users

```bash
curl -X GET "http://127.0.0.1:8000/v1/users"
```

**Expected Output:**

```json
[
  {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com"
  }
]
```

---

### 3️⃣ Version 2: Create User

```bash
curl -X POST "http://127.0.0.1:8000/v2/users" \
-H "Content-Type: application/json" \
-d '{"id":2,"name":"Bob","email":"bob@example.com","is_active":false}'
```

**Expected Output:**

```json
{
  "id": 2,
  "name": "Bob",
  "email": "bob@example.com",
  "is_active": false
}
```

---

### 4️⃣ Version 2: Get Users

```bash
curl -X GET "http://127.0.0.1:8000/v2/users"
```

**Expected Output:**

```json
[
  {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "is_active": true
  },
  {
    "id": 2,
    "name": "Bob",
    "email": "bob@example.com",
    "is_active": false
  }
]
```

---

### ✅ Key Learning Points

* Versioned endpoints: `/v1/users` and `/v2/users`
* v2 can **handle older User objects** seamlessly
* Introduced `is_active` field in v2 without breaking v1
* FastAPI + Pydantic handles validation and serialization automatically

---

### Step 6: Cleanup (Optional)

```bash
deactivate
```
