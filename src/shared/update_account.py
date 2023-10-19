import json
from src.shared.generate_hash import generate_hash_password, encode, decode

def update_account(user_id):
    new_name = input('Enter new name: ')
    new_tel = input('Enter new telephone number: ')
    new_age = input('Enter new age: ')

    # Read and write new account details to data file
    with open("user_data_storage.json", 'r') as data_file:
        f_data = json.load(data_file)
        details = f_data['personal_details']
        for detail in details:
            if user_id == str(detail['id']):
                detail['name'] = new_name
                detail['age'] = new_age
                detail['tel'] = encode(new_tel)

    with open("user_data_storage.json", 'w') as f_outfile:
        json.dump(f_data, f_outfile)

    print("Account update is successful")


def view_account(user_id):
    # Read account details from data file
    with open("user_data_storage.json", 'r') as data_file:
        f_data = json.load(data_file)
        details = f_data['personal_details']
        for detail in details:
            if user_id == str(detail['id']):
                print("Account name: " + detail['name'])
                print("Age: " + detail['age'])
                print("NIC number: " + decode(detail['nic_no']))
                print("Telephone: " + decode(detail['tel']))

def renew_password(user_id):
    new_pwd = input('Enter a password including a lower-case letter, an upper-case letter, a digit, and length not '
                    'less than 6: \n')

    while True:
        if not (any(x.isupper() for x in new_pwd) and any(x.islower() for x in new_pwd) and any(
                x.isdigit() for x in new_pwd) and len(new_pwd) >= 6):
            new_pwd = input("Password is weak. Please re-try: ")
        else:
            break

    new_password = generate_hash_password(new_pwd)

    with open("configuration_storage.json", 'r') as data_file:
        f_data = json.load(data_file)
        account = f_data['users']
        for user in account:
            if user_id == str(user['id']):
                user['password'] = new_password

    with open("configuration_storage.json", 'w') as f_outfile:
        json.dump(f_data, f_outfile)

    print("Password updated successfully")
