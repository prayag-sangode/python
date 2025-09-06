from flask import Flask, request, jsonify

app = Flask(__name__)

# GET request with query parameters
@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "Guest")
    return jsonify({"message": f"Hello, {name}!"})

# POST request with JSON body
@app.route("/sum", methods=["POST"])
def sum_numbers():
    data = request.get_json()
    if not data or "a" not in data or "b" not in data:
        return jsonify({"error": "Please provide 'a' and 'b' in JSON body"}), 400
    result = data["a"] + data["b"]
    return jsonify({"a": data["a"], "b": data["b"], "sum": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
