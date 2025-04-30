from flask import Flask
app = Flask(__name__)

# Añade el método jsonify a tu importación de Flask
from flask import Flask, jsonify, request

# Supongamos que tienes tus datos en la variable some_data
some_data = { "name": "Bobby", "lastname": "Rixer" }

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    # Puedes convertir esa variable en una cadena json de la siguiente manera
    json_text = jsonify(todos)

    # Y luego puedes devolverlo al front-end en el cuerpo de la respuesta de la siguiente manera
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todos(position):

    if position < 0 or position >= len(todos):
        return jsonify({"error": "Posición no válida"}), 404
    
    del todos[position]
    
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)