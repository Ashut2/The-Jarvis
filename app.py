# setting up the flask api that take task and add them 
from flask import Flask, request, jsonify

app = Flask(__name__)

# Example endpoint for adding tasks
tasks = []

@app.route('/add-task', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')
    if task:
        tasks.append(task)
        return jsonify({"message": "Task added successfully!"}), 201
    return jsonify({"error": "Task not provided"}), 400

# Example endpoint for fetching all tasks
@app.route('/get-tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

if __name__ == '__main__':
    app.run(debug=True)
