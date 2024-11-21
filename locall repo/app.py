# setting up the flask api that take task and add them 
from flask import Flask, request, jsonify

app = Flask(__name__)

# Creating  endpoint for adding tasks
tasks = []

@app.route('/add-task', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')
    if task:
        tasks.append(task)
        return jsonify({"message": "Task added successfully!"}), 201
    return jsonify({"error": "Task not provided"}), 400

# Creating  endpoint for fetching all tasks
@app.route('/get-tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route("/delete-task" , methods=['POST'])
def remove_task():
    data = request.get_json()
    if 'task' not in data:
        return jsonify({"message": "No task provided"}), 400
    
    task = data.get('task')
    if task in tasks :
        tasks.remove(task)
        return jsonify({"message": "Task deleted Successfully!"}) , 200  
    return jsonify({"error" : "Task Not Found"}) , 404

# error handling code for deleting tasks



if __name__ == '__main__':
    app.run(debug=True)


# For simplicity, we’ll assume each task is a string, and “completed” status could be handled with a more complex data structure.