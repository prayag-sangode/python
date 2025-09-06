# Lab 21: Flask CRUD API

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab21
cd ~/python/labs/lab21
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
flask
sqlalchemy
EOF
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Step 3: Create Flask App `app.py`

```bash
cat >> app.py << EOF
from flask import Flask, request, jsonify
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Initialize Flask
app = Flask(__name__)

# SQLAlchemy setup
Base = declarative_base()
engine = create_engine("sqlite:///notes.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Note model
class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "content": self.content}

# Create tables
Base.metadata.create_all(engine)

# --- CRUD Routes ---

# Create a note
@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json()
    if not data or "title" not in data or "content" not in data:
        return jsonify({"error": "title and content required"}), 400
    note = Note(title=data["title"], content=data["content"])
    session.add(note)
    session.commit()
    return jsonify(note.to_dict()), 201

# Read all notes
@app.route("/notes", methods=["GET"])
def get_notes():
    notes = session.query(Note).all()
    return jsonify([note.to_dict() for note in notes])

# Read a single note
@app.route("/notes/<int:note_id>", methods=["GET"])
def get_note(note_id):
    note = session.query(Note).get(note_id)
    if not note:
        return jsonify({"error": "Note not found"}), 404
    return jsonify(note.to_dict())

# Update a note
@app.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    data = request.get_json()
    note = session.query(Note).get(note_id)
    if not note:
        return jsonify({"error": "Note not found"}), 404
    if "title" in data:
        note.title = data["title"]
    if "content" in data:
        note.content = data["content"]
    session.commit()
    return jsonify(note.to_dict())

# Delete a note
@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    note = session.query(Note).get(note_id)
    if not note:
        return jsonify({"error": "Note not found"}), 404
    session.delete(note)
    session.commit()
    return jsonify({"message": f"Note {note_id} deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
EOF
```

---

## Step 4: Run the Flask App

```bash
python app.py
```

* Server runs at **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## Step 5: Test the API

### Create a note

```bash
curl -X POST "http://127.0.0.1:5000/notes" -H "Content-Type: application/json" -d '{"title":"First Note","content":"This is a test note"}'
```

**Output:**

```json
{"id":1,"title":"First Note","content":"This is a test note"}
```

### Get all notes

```bash
curl http://127.0.0.1:5000/notes
```

**Output:**

```json
[{"id":1,"title":"First Note","content":"This is a test note"}]
```

### Get single note

```bash
curl http://127.0.0.1:5000/notes/1
```

**Output:**

```json
{"id":1,"title":"First Note","content":"This is a test note"}
```

### Update note

```bash
curl -X PUT "http://127.0.0.1:5000/notes/1" -H "Content-Type: application/json" -d '{"content":"Updated content"}'
```

**Output:**

```json
{"id":1,"title":"First Note","content":"Updated content"}
```

### Delete note

```bash
curl -X DELETE http://127.0.0.1:5000/notes/1
```

**Output:**

```json
{"message":"Note 1 deleted"}
```

---

### Key Learning Points

* Full **CRUD API** with Flask
* Use **SQLAlchemy ORM** for database operations
* Handle **JSON requests** and **JSON responses**
* Proper **status codes** for success and errors

