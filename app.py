from flask import Flask, jsonify

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Sweta", "department": "IT"},
    {"id": 2, "name": "Rahul", "department": "HR"}
]

@app.route("/")
def home():
    return "Employee Flask Application"

@app.route("/employees")
def get_employees():
    return jsonify(employees)

if __name__ == "__main__":
    app.run(debug=True)