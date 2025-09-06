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
