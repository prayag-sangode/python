from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Versioned API Example")

# Pydantic model
class User(BaseModel):
    id: int
    name: str
    email: str

# In-memory DB
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
# v2 introduces 'is_active' field
class UserV2(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True

@app.get("/v2/users", response_model=List[UserV2])
def get_users_v2():
    # Convert old users to v2 by adding default is_active=True
    return [UserV2(**user.dict(), is_active=True) for user in users_db]

@app.post("/v2/users", response_model=UserV2)
def create_user_v2(user: UserV2):
    users_db.append(user)
    return user
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
