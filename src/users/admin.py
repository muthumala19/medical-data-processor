import json
from src.shared.generate_hash import generate_hash_password, encode
def create_admin():
    name = input('Admin username: ')
    temp_password = generate_hash_password(input('Temporary password: '))

    with open("configuration_storage.json", 'r') as json_data_file:
        data = json.load(json_data_file)
        admin_id = len(data['users']) + 1
        data['users'].append({
            'id': admin_id,
            'name': name,
            'password': temp_password,
            'user_type': "admin",
            'privilege_level': '1'
        })

    with open("configuration_storage.json", 'w') as outfile:
        json.dump(data, outfile)

    print("Account created successfully")
    print("Please enter personal details of admin")

    admin_name = input('Admin name: ')
    age = input('Age: ')
    nic_no = input('NIC number: ')
    tel = input('Telephone number: ')

    with open("user_data_storage.json", 'r') as json_data_file:
        data = json.load(json_data_file)
        data['personal_details'].append({
            'id': admin_id,
            'name': admin_name,
            'age': age,
            'nic_no': encode(nic_no),
            'tel': encode(tel)
        })

    with open("user_data_storage.json", 'w') as outfile:
        json.dump(data, outfile)


def change_codes():
    doctor, receptionist = '', ''
    print(
        "Press 1 to edit doctor code\nPress 2 to edit receptionist code\nPress 3 to create admin account\nPress "
        "-1 to exit\n")

    while True:
        role_number = input()
        if role_number == '1':
            doctor = generate_hash_password(input("Enter new doctor code: "))
        elif role_number == '2':
            receptionist = generate_hash_password(input("Enter new receptionist code: "))
        elif role_number == '3':
            create_admin()
        elif role_number == '-1':
            print("Thank you admin")
            break
        else:
            print("Invalid input")

    return doctor, receptionist


class Admin:
    def update_codes(self):
        doctor, receptionist = change_codes()
        self.change_config(doctor, receptionist)

    @staticmethod
    def change_config(doctor_code, receptionist_code):
        with open("configuration_storage.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            data['codes']['doctor'] = doctor_code
            data['codes']['receptionist'] = receptionist_code

        with open("configuration_storage.json", 'w') as outfile:
            json.dump(data, outfile)
