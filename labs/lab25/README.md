# Lab 25: FastAPI CRUD API

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab25
cd ~/python/labs/lab25
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

## Step 3: Create FastAPI App `main.py`

```bash
cat >> main.py << EOF
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Pydantic model for request/response
class Note(BaseModel):
    id: int
    title: str
    content: Optional[str] = None

# In-memory "database"
notes_db: List[Note] = []

# CREATE a note
@app.post("/notes/", response_model=Note)
def create_note(note: Note):
    # Check for duplicate id
    for n in notes_db:
        if n.id == note.id:
            raise HTTPException(status_code=400, detail="Note ID already exists")
    notes_db.append(note)
    return note

# READ all notes
@app.get("/notes/", response_model=List[Note])
def get_notes():
    return notes_db

# READ single note by ID
@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    for note in notes_db:
        if note.id == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")

# UPDATE a note
@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, updated_note: Note):
    for idx, note in enumerate(notes_db):
        if note.id == note_id:
            notes_db[idx] = updated_note
            return updated_note
    raise HTTPException(status_code=404, detail="Note not found")

# DELETE a note
@app.delete("/notes/{note_id}", response_model=dict)
def delete_note(note_id: int):
    for idx, note in enumerate(notes_db):
        if note.id == note_id:
            del notes_db[idx]
            return {"message": f"Note {note_id} deleted"}
    raise HTTPException(status_code=404, detail="Note not found")
EOF
```

---

## Step 4: Run the FastAPI App

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

* Server runs at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**
* Interactive docs:

  * Swagger UI: `http://127.0.0.1:8000/docs`
  * Redoc: `http://127.0.0.1:8000/redoc`

> Press `Ctrl+C` to stop the server.

---

## Step 5: Test Endpoints

### Create a Note

```bash
curl -X POST "http://127.0.0.1:8000/notes/" \
-H "Content-Type: application/json" \
-d '{"id":1,"title":"First Note","content":"This is the first note."}'
```

**Expected Output:**

```json
{
  "id": 1,
  "title": "First Note",
  "content": "This is the first note."
}
```

---

### Read All Notes

```bash
curl -X GET "http://127.0.0.1:8000/notes/"
```

**Expected Output:**

```json
[
  {
    "id": 1,
    "title": "First Note",
    "content": "This is the first note."
  }
]
```

---

### Read Single Note by ID

```bash
curl -X GET "http://127.0.0.1:8000/notes/1"
```

**Expected Output:**

```json
{
  "id": 1,
  "title": "First Note",
  "content": "This is the first note."
}
```

---

### Update a Note

```bash
curl -X PUT "http://127.0.0.1:8000/notes/1" \
-H "Content-Type: application/json" \
-d '{"id":1,"title":"Updated Note","content":"Updated content"}'
```

**Expected Output:**

```json
{
  "id": 1,
  "title": "Updated Note",
  "content": "Updated content"
}
```

---

### Delete a Note

```bash
curl -X DELETE "http://127.0.0.1:8000/notes/1"
```

**Expected Output:**

```json
{"message":"Note 1 deleted"}
```

---

### Key Learning Points

* Implement full **CRUD operations** with FastAPI
* Use **Pydantic models** for input/output validation
* Handle **HTTP exceptions** with `HTTPException`
* Maintain a **temporary in-memory database** (later can extend to SQLAlchemy/real DB)
* Test endpoints with **curl or Swagger UI**

---

### Step 6: Cleanup (Optional)

```bash
deactivate
```
