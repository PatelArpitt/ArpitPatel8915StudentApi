from flask import Flask, request, jsonify

app = Flask(__name__)
students = [
    {'id': 1, 'name': 'Arpit', 'grade': 89},
    {'id': 2, 'name': 'Balmukund', 'grade': 78},
    {'id': 3, 'name': 'Chameli', 'grade': 69}
]

# Get a list of all students [GET REQUEST]
@app.route('/students', methods = ['GET'])
def get_students():
    return jsonify({'info': 'All students listed', 'data': students}), 200

# Read a student by ID [GET REQUEST]
@app.route('/students/<int:student_id>', methods = ['GET'])
def read_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify({'info': f'Student: {student_id} listed', 'data': student}), 200

# Create a new student [POST REQUEST]
@app.route('/students', methods = ['POST'])
def create_student():
    data = request.get_json()
    student = {
        'id': data['id'],
        'name': data['name'],
        'grade': data['grade']
    }
    students.append(student)
    return jsonify({'info': 'New student created', 'data': student}), 201

# Update a student by ID [PUT REQUEST]
@app.route('/students/<int:student_id>', methods = ['PUT'])
def update_student(student_id):
    data = request.get_json()
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    student.update(data)
    return jsonify({'info': f'Student: {student_id} updated', 'data': student}), 201

# Delete a student by ID [DELETE REQUEST]
@app.route('/students/<int:student_id>', methods = ['DELETE'])
def delete_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    students.remove(student)
    return jsonify({'info': f'Student: {student_id} deleted', 'data': student}), 200


if __name__ == '__main__':
    app.run(debug = False)