from src.auth.signin import SignIn
from src.users.admin import Admin
from src.users.receptionist import Receptionist
from src.users.doctor import Doctor
from src.users.patient import Patient
from src.shared.edit_account import edit_account, renew_password, view_account
from src.shared.check_patient_id import check_patient_id


def main():
    current_user = SignIn().auth_user()
    if current_user:
        current_user_id = str(current_user.get('id'))
        privilege_level = current_user.get('privilege_level')

        if privilege_level == '1':  # Admin
            Admin().set_codes()

        elif privilege_level == '3':  # Receptionist
            handle_receptionist_actions(current_user_id)

        elif privilege_level == '2':  # Doctor
            handle_doctor_actions(current_user_id)

        elif privilege_level == '4':  # Patient
            handle_patient_actions(current_user_id)


def handle_receptionist_actions(user_id):
    print(
        "Press 1 to create patient account\nPress 2 to edit personal account\nPress 3 to view personal account\nPress "
        "4 to set new password\nPress -1 to exit\n ")

    while True:
        option = input()
        if option == '1':
            Receptionist().create_patient_account()
        elif option == '2':
            edit_account(user_id)
        elif option == '3':
            view_account(user_id)
        elif option == '4':
            renew_password(user_id)
        elif option == '-1':
            print("Thank you receptionist")
            break
        else:
            print("Invalid input. Try again")


def handle_doctor_actions(user_id):
    print(
        "Press 1 to add sickness details \nPress 2 to add drug prescription \nPress 3 to add lab test prescription "
        "\nPress 4 to view sickness details \nPress 5 to view previous drug prescriptions \nPress 6 to view lab test "
        "prescription \nPress 7 to edit account \nPress 8 to renew password \nPress 9 to view account\nPress -1 to "
        "exit\n ")

    while True:
        option = input()
        if option in ['1', '2', '3', '4', '5', '6']:
            while True:
                patient_id = input("Enter patient id: ")
                if check_patient_id(patient_id):
                    break
                else:
                    print("Invalid patient id")
            if option == '1':
                Doctor().add_sickness_details(patient_id)
            elif option == '2':
                Doctor().add_drug_prescription(patient_id)
            elif option == '3':
                Doctor().add_labtest_prescription(patient_id)
            elif option == '4':
                Doctor().read_sickness_details(patient_id)
            elif option == '5':
                Doctor().read_drug_prescription(patient_id)
            elif option == '6':
                Doctor().read_labtest_prescription(patient_id)
        elif option == '7':
            edit_account(user_id)
        elif option == '8':
            renew_password(user_id)
        elif option == '9':
            view_account(user_id)
        elif option == '-1':
            print("Thank you doctor")
            break
        else:
            print("Invalid input. Try again")


def handle_patient_actions(user_id):
    print(
        "Press 1 to change password \nPress 2 to update account \nPress 3 to view account details\nPress 4 to view "
        "sickness details \nPress 5 to view previous drug prescriptions \nPress 6 to view lab test prescription "
        "\nPress -1 to exit\n ")

    while True:
        option = input()
        if option == '1':
            renew_password(user_id)
        elif option == '2':
            edit_account(user_id)
        elif option == '3':
            view_account(user_id)
        elif option == '4':
            Patient().read_sickness_details(user_id)
        elif option == '5':
            Patient().read_drug_prescription(user_id)
        elif option == '6':
            Patient().read_labtest_prescription(user_id)
        elif option == '-1':
            print("Thank you")
            break
        else:
            print("Invalid input. Try again")
