# restful_api_flask

## Use Original flask to build api
```
python3 my_flask_api.py
```
- Host Status
  * URL: http://127.0.0.1:5000
  * Return:
    ```
    {"host": "on"}
    ```
- GET (List all users)
  * URL: http://127.0.0.1:5000/users
  * Return:
    ```
    [
      {
          "password": "password1",
          "username": "user1"
      },
      {
          "password": "password2",
          "username": "user2"
      }
    ]
    ```
- POST (Create new user)
  * URL: http://127.0.0.1:5000/users
  * Body/Row/Json:
    ```
    {"username": "user3",
     "password": "password3"
    }
    ```
  * Return:
    ```
    {"message": "user created"}
    ```
    ```
    {"message": "user has existed"}
    ```
- DELETE (Delete user)
  * URL: http://127.0.0.1:5000/users/<username>
  * Return:
    ```
    {"message": "user deleted"}
    ```
    ```
    {"message": "user doesn't exist"}
    ```
- PUT (Update user's password)
  * URL: http://127.0.0.1:5000/users/<username>
  * Body/Row/Json: 
    ```
    {"password": "username's password"}
    ```
  * Return:
    ```
    {"message": "user username's password changed"}
    ```
    ```
    {"message": "user doesn't exist"}
    ```
