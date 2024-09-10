from flask import Flask, request, jsonify
from ...application.use_cases import CreateUser
from ...adapters.repositories.sql_repository import SQLUserRepository

app = Flask(__name__)

user_repository = SQLUserRepository()
create_user_use_case = CreateUser(user_repository)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    
    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400
    
    try:
        new_user = create_user_use_case.execute(name, email)
        return jsonify({
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = user_repository.get(user_id)
        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)
