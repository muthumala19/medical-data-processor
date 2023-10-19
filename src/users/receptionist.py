import json
from src.controllers.generate_hash import generate_hash_password, encode
class Receptionist:
    @staticmethod
    def create_account(user_type, privilege_level):
        username = input(f'{user_type} username: ')
        temp_password = generate_hash_password(input('Password: '))
        # Read and write user to config file
        with open("configuration_storage.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            user_id = len(data['users']) + 1
            data['users'].append({
                'id': user_id,
                'name': username,
                'password': temp_password,
                'user_type': user_type,
                'privilege_level': privilege_level
            })
        with open("configuration_storage.json", 'w') as outfile:
            json.dump(data, outfile)
        print("\nAccount creation successful!\n")
        print(f"Please enter personal details of {user_type}")
        user_name = input(f'{user_type} name: ')
        age = input('Age: ')
        nic_no = input('NIC number: ')
        tel = input('Telephone number: ')
        # Read and write user details to data file
        with open("user_data_storage.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            data['personal_details'].append({
                'id': user_id,
                'name': user_name,
                'age': age,
                'nic_no': encode(nic_no),
                'tel': encode(tel)
            })

        with open("user_data_storage.json", 'w') as outfile:
            json.dump(data, outfile)
    @staticmethod
    def create_patient():
        Receptionist.create_account("patient", "4")
