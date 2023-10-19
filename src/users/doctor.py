import json
from datetime import datetime


class Doctor:
    @staticmethod
    def update_details(patient_id, data_key, message):
        details = input(f"Enter {message}: \n")

        with open("user_data_storage.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            data[data_key].append({
                'id': patient_id,
                data_key: details,
                'date': str(datetime.now())[:19],
            })

        with open("user_data_storage.json", 'w') as outfile:
            json.dump(data, outfile)

        print(f"{message} added")

    @staticmethod
    def display_details(patient_id, data_key, detail_name):
        with open("user_data_storage.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data[data_key]

            for detail in details:
                if detail['id'] == patient_id:
                    print(f"{detail['date']} - {detail[detail_name]}")

    @staticmethod
    def update_sickness_details(patient_id):
        Doctor.update_details(patient_id, 'sickness_details', 'sickness details')

    @staticmethod
    def update_drug_prescription(patient_id):
        Doctor.update_details(patient_id, 'drug_presc', 'drug prescription')

    @staticmethod
    def update_labtest_prescription(patient_id):
        Doctor.update_details(patient_id, 'labtest_presc', 'lab test prescription')

    @staticmethod
    def display_sickness_details(patient_id):
        Doctor.display_details(patient_id, 'sickness_details', 'sickness')

    @staticmethod
    def display_drug_prescription(patient_id):
        Doctor.display_details(patient_id, 'drug_presc', 'drug_presc')

    @staticmethod
    def display_labtest_prescription(patient_id):
        Doctor.display_details(patient_id, 'labtest_presc', 'labtest_presc')
