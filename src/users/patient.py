import json

class Patient:

    @staticmethod
    def display_details(patient_id, data_key, detail_name):
        with open("user_data_storage.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data[data_key]

            for detail in details:
                if detail['id'] == patient_id:
                    print(f"{detail['date']} - {detail[detail_name]}")

    @staticmethod
    def display_sickness_details(patient_id):
        Patient.display_details(patient_id, 'sickness_details', 'sickness')

    @staticmethod
    def read_drug_prescription(patient_id):
        Patient.display_details(patient_id, 'drug_presc', 'drug_presc')

    @staticmethod
    def read_labtest_prescription(patient_id):
        Patient.display_details(patient_id, 'labtest_presc', 'labtest_presc')
