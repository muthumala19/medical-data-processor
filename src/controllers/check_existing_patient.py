import json
def check_existing_patients(id):
    with open("configuration_storage.json", 'r') as file:
        data = json.load(file)
        patients = data['users']
        for patient in patients:
            if id == str(patient['id']) and patient['user_type'] == 'patient':
                return True
        return False
