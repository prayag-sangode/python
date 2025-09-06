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
