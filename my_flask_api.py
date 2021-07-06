from logging import debug

from flask import Flask
from flask.globals import request
from flask.json import jsonify
from werkzeug.exceptions import RequestTimeout

app = Flask(__name__)

### hoat Status
@app.route("/")
def host_status():
    return {"host":"on"}



user_list = [
    {
        "username": "Tom",
        "password": "tompsd"
    },
    {
        "username":"Jerry",
        "password": "jerrypsd"
    }
]

### User Information
# get
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(user_list)

# post
@app.route("/users", methods=["POST"])
def create_user():
    user = request.get_json()
    print(user)
    if user['username'] not in [item["username"] for item in user_list]:
        user_list.append(user)
        return jsonify({"message": "user created"})
    else:
        return jsonify({"message": "user has existed"})

# # delete
# @app.route("/users/<username>", methods=["DELETE"])
# def delete_user(username):
#     for item in user_list:
#         if item["username"] == username:
#             user_list.remove(item)
#             return {"message":"user deleted"}
#     return jsonify({"message": "user doesn't exist"})


# # delete & put
@app.route("/users/<username>", methods=["DELETE", "PUT"])
def delete_user(username):
    for user in user_list:
        if user["username"] == username:
            if request.method == "DELETE":
                user_list.remove(user)
                return {"message":"user deleted"}
            elif request.method == "PUT":
                index = user_list.index(user)
                user["password"] = request.get_json()["password"]
                user_list[index] = user
                return jsonify({"message": "user {}'s password changed".format(user["username"])})
    return jsonify({"message": "user doesn't exist"})




if __name__ == "__main__":
    app.run()
