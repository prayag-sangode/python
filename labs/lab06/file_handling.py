import json

# ----------- TEXT FILE HANDLING -----------
# Write to a text file
with open("sample.txt", "w") as f:
    f.write("Hello, this is a text file.\n")
    f.write("This is another line.\n")

# Read from a text file
with open("sample.txt", "r") as f:
    content = f.read()
    print("Text file content:")
    print(content)

# ----------- JSON FILE HANDLING -----------
data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Flask", "FastAPI"]
}

# Write JSON to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Read JSON from file
with open("data.json", "r") as f:
    loaded_data = json.load(f)
    print("JSON file content:")
    print(loaded_data)
