import json
from src.controllers.generate_hash import generate_hash_password


class SignIn:

    @staticmethod
    def authenticate():
        name = input("Enter username: ")
        hashed_password = generate_hash_password(input("Enter password: "))

        with open("configuration_storage.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            current_user = SignIn.find_user(data['users'], name, hashed_password)

        if current_user:
            print("Sign in successful")
            return current_user
        else:
            print("Sign in failed")
            return False

    @staticmethod
    def find_user(users, username, password):
        for user in users:
            if username == user['name'] and password == user['password']:
                return user
        return None
