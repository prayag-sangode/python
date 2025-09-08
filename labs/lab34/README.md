# Lab 34: Role-Based Access Control (RBAC) with FastAPI

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab34
cd ~/python/labs/lab34
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
python-multipart
passlib[bcrypt]
pyjwt
EOF
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Step 3: Create FastAPI App `main.py`

```bash
cat >> main.py << EOF
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from typing import Optional

# JWT settings
SECRET_KEY = "myjwtsecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI(title="RBAC with JWT Lab")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Fake user DB with roles
fake_users_db = {
    "admin": {
        "username": "admin",
        "full_name": "Admin User",
        "hashed_password": pwd_context.hash("admin123"),
        "role": "admin",
    },
    "user": {
        "username": "user",
        "full_name": "Normal User",
        "hashed_password": pwd_context.hash("user123"),
        "role": "user",
    }
}

# Utility functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None or username not in fake_users_db:
            raise HTTPException(status_code=401, detail="Invalid token")
        return fake_users_db[username]
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Token endpoint
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"], "role": user["role"]},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Role-based dependency
def require_role(role: str):
    def role_checker(user: dict = Depends(get_current_user)):
        if user["role"] != role:
            raise HTTPException(status_code=403, detail="Operation forbidden")
        return user
    return role_checker

# Protected routes
@app.get("/admin-data")
def admin_data(user: dict = Depends(require_role("admin"))):
    return {"message": f"Hello {user['username']}, this is admin-only data."}

@app.get("/user-data")
def user_data(user: dict = Depends(require_role("user"))):
    return {"message": f"Hello {user['username']}, this is user-only data."}

@app.get("/common-data")
def common_data(user: dict = Depends(get_current_user)):
    return {"message": f"Hello {user['username']}, this data is accessible to any logged-in user."}
EOF
```

---

## Step 4: Run FastAPI App

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Server runs at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.

---

## Step 5: Test RBAC

### 1️⃣ Obtain JWT Token (Admin)

```bash
curl -X POST "http://127.0.0.1:8000/token" \
  -d "username=admin&password=admin123" \
  -H "Content-Type: application/x-www-form-urlencoded"
```

### 2️⃣ Access Admin Route

```bash
curl -H "Authorization: Bearer <JWT_TOKEN>" http://127.0.0.1:8000/admin-data
```

**Expected:** Success.

### 3️⃣ Access User Route as Admin

```bash
curl -H "Authorization: Bearer <JWT_TOKEN>" http://127.0.0.1:8000/user-data
```

**Expected:** 403 Forbidden.

### 4️⃣ Common Route

```bash
curl -H "Authorization: Bearer <JWT_TOKEN>" http://127.0.0.1:8000/common-data
```

**Expected:** Accessible for both admin and user.

---

## Step 6: Key Learning Points

* Role is stored in JWT token.
* `Depends` + custom function enforces role-based access.
* Routes can be restricted to specific roles (`admin`, `user`).
* Any logged-in user can access common routes.
* This lab extends JWT authentication to **RBAC**.


