from flask import Flask, jsonify, request
from flask.wrappers import Request

app = Flask(__name__)


user_list = [
    {
        'username':'Tom',
        'password':'tompass'
    },
    {
        'username':'John',
        'password':'johnpass'
    }
]


@app.route('/')
def home():
    return "Here is home."

# GET
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(user_list)

# POST
@app.route('/user', methods=['POST'])
def create_user():
    user = request.get_json()
    # check if user already exist
    user_check = list(filter(lambda x: user.get('username')==x['username'], user_list))
    if not user_check:
        user_list.append(user)
        return jsonify({'message': 'user created!'})
    else:
        return jsonify({'message': 'user already exist!'})


# DELETE
# @app.route('/user/<username>', methods=['DELETE'])
# def delete_user(username):
#     for user in user_list:
#         if user['username'] == username:
#             user_list.remove(user)
#             return jsonify({'message': 'user deleted!'})
#     return jsonify({'message': "Can't find this user"})


# DELETE and PUT (two methods in one route)
@app.route('/user/<username>', methods=['PUT', 'DELETE'])
def update_user(username):
    user_find = False
    for user in user_list:
        if user['username'] == username:
            user_find = True
            break
    if not user_find:
        return jsonify({'message': 'user not found.'})
    if request.method == 'DELETE':
        user_list.remove(username)
        return jsonify({'message': 'user deleted!'})
    elif request.method == 'PUT':
        new_password = request.get_json()
        user_list.remove(user)
        user_list.append({'username': username,
        'password': new_password['password']})
        return jsonify({'message': 'user password updated.'})



if __name__ == '__main__':
    app.run()
    