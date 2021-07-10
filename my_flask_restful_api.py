from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

user_list = []

def min_length_str(min_length):
    def validate(s):
        print(type(s), s)
        if not s:
            raise Exception('password required!')
        if not isinstance(s, (int, str)):
            raise Exception('password format error')
        s = str(s)
        if len(s) >= min_length:
            return s
        raise Exception(f'String must at least {min_length} characters long')
    return validate

class HostStatus(Resource):
    def get(self):
        return {"host":"on"}


class UserList(Resource):
    def get(self):
        return user_list

class User(Resource):
    # reqparse 可以幫助判定輸入的data正確性
    parser = reqparse.RequestParser()
    parser.add_argument('password', type=min_length_str(5), required=True,
                        help='{error_msg}')
    # get user detail information
    def get(self, username):
        for user in user_list:
            if user['username'] == username:
                return user
        return {"message": "User not found"}, 404

    # create a user
    def post(self, username):
        data = User.parser.parse_args()
        print(data)
        user = {
            "username": username,
            "password": data.get("password")
        }
        if user["username"] not in [item["username"] for item in user_list]:
            user_list.append(user)
            return user, 201
        return {"message": "User exists"}

    # delete a user
    def delete(self, username):
        for user in user_list:
            if user["username"] == username:
                user_list.remove(user)
                return {"message": "User deleted"}
        return {"message": "User not found"}, 204

    def put(self, username):
        for user in user_list:
            if user["username"] == username:
                data = User.parser.parse_args()
                # index = user_list.index(user)
                user["password"] = data.get("password")
                # user_list[index] = user
                return user
        return {"message": "User not found"}, 204



api.add_resource(HostStatus, '/')
api.add_resource(UserList, '/users')
api.add_resource(User, '/user/<string:username>')



if __name__ == '__main__':
    app.run()
