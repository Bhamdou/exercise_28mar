from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Alice", "job": "Software Developer"},
    {"id": 2, "name": "Bob", "job": "Product Manager"},
]

@app.route('/api/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/api/employees', methods=['POST'])
def add_employee():
    employee = request.get_json()
    employees.append(employee)
    return jsonify(employee), 201

@app.route('/api/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = next((e for e in employees if e["id"] == employee_id), None)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404

@app.route('/api/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employee = next((e for e in employees if e["id"] == employee_id), None)
    if employee:
        updated_employee = request.get_json()
        employee.update(updated_employee)
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404

@app.route('/api/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    global employees
    employees = [e for e in employees if e["id"] != employee_id]
    return jsonify({"result": "Employee deleted"})

if __name__ == '__main__':
    app.run(debug=True)
