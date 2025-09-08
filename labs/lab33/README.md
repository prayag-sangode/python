# Lab 33: JWT Authentication with FastAPI

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab33
cd ~/python/labs/lab33
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
from fastapi import FastAPI, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from typing import Optional

# Secret key
SECRET_KEY = "myjwtsecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI(title="JWT Authentication Lab")

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Fake user database
fake_users_db = {
    "prayag": {
        "username": "prayag",
        "full_name": "Prayag Sangode",
        "email": "prayag@example.com",
        "hashed_password": pwd_context.hash("password123"),
        "disabled": False,
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

# Token endpoint
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Protected route
@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None or username not in fake_users_db:
            raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": username, "email": fake_users_db[username]["email"]}
EOF
```

---

## Step 4: Run the FastAPI App

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Server will run at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**. Swagger docs available at `/docs`.

---

## Step 5: Test JWT Authentication

### Obtain JWT Token

```bash
curl -X POST "http://127.0.0.1:8000/token" \
  -d "username=prayag&password=password123" \
  -H "Content-Type: application/x-www-form-urlencoded"
```

**Expected Response:**

```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

### Access Protected Route

```bash
curl -X GET "http://127.0.0.1:8000/users/me" \
  -H "Authorization: Bearer <JWT_TOKEN>"
```

**Expected Response:**

```json
{
  "username": "prayag",
  "email": "prayag@example.com"
}
```

---

## Step 6: Key Learning Points

* `OAuth2PasswordBearer` + `Form` for login.
* `python-multipart` required to parse form data.
* JWT generated using `pyjwt`.
* Protected routes require valid bearer token.
* Passwords are hashed using `passlib[bcrypt]`.

