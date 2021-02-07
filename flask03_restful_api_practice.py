from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

user_list = []


def min_length_str(min_length):
    def validation(s):
        if s is None:
            raise Exception('password required')
        if not isinstance(s, (int, str)):
            raise Exception('password format error')
        str(s)
        if len(s) >= min_length:
            return s
        raise Exception(f'String must be at least {min_length} characters long.')
    return validation


class Helloworld(Resource):
    def get(self):
        return 'hello flask api'


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password', type=min_length_str(5), required=True,
                        help='{error_msg}')
    def get(self, username):
        """Get user detail information"""
        for user in user_list:
            if user['username'] == username:
                return user
        return {'message': 'user not found'}, 404  # 404 not found

    def post(self, username):
        """Create new user"""
        data = User.parser.parse_args()
        user = {
            'username': username,
            'password': data.get('password')
        }
        for user in user_list:
            if user['username'] == username:
                return {'message': 'user already exist'}
        user_list.append(user)
        return user, 201

    def delete(self, username):
        """Delete user"""
        user_find = False
        for user in user_list:
            if user['username'] == username:
                user_find = True
                break
        if user_find:
            user_list.remove(user)
            return {'message': 'user deleted'}
        else:
            return {'message': 'user not found'}, 204  # 204 no content

    def put(self, username):
        """Update user information"""
        user_find = False
        for user in user_list:
            if user['username'] == username:
                user_find = True
                break
        if user_find:
            data = User.parser.parse_args()
            user_list.remove(user)
            user['password'] = data['password']
            user_list.append(user)
            return user
        else:
            return {'message':'user not found'}, 204 # 204 no content


class UserList(Resource):
    def get(self):
        """Get user list"""
        return user_list


api.add_resource(Helloworld, '/')
api.add_resource(User, '/user/<string:username>')
api.add_resource(UserList, '/users')


if __name__ == '__main__':
    app.run()
