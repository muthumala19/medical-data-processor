from src.auth.signin import SignIn
from src.users.admin import Admin
from src.users.receptionist import Receptionist
from src.users.doctor import Doctor
from src.users.patient import Patient
from src.shared.update_account import update_account, renew_password, view_account
from src.shared.check_existing_patient import check_existing_patients


def main():
    current_user = SignIn().authenticate()
    if current_user:
        current_user_id = str(current_user.get('id'))
        privilege_level = current_user.get('privilege_level')

        if privilege_level == '1':  # Admin
            Admin().update_codes()

        elif privilege_level == '3':  # Receptionist
            handle_receptionist_actions(current_user_id)

        elif privilege_level == '2':  # Doctor
            handle_doctor_actions(current_user_id)

        elif privilege_level == '4':  # Patient
            handle_patient_actions(current_user_id)


def handle_receptionist_actions(user_id):
    print("Press :"
          "\n     1 to create patient account"
          "\n     2 to edit personal account"
          "\n     3 to view personal account"
          "\n     4 to set new password"
          "\n     -1 to exit\n ")

    while True:
        option = input()
        if option == '1':
            Receptionist().create_patient()
        elif option == '2':
            update_account(user_id)
        elif option == '3':
            view_account(user_id)
        elif option == '4':
            renew_password(user_id)
        elif option == '-1':
            print("Thank you!")
            break
        else:
            print("Invalid input!")


def handle_doctor_actions(user_id):
    print(
        "Press :"
        "\n     1 to add sickness details "
        "\n     2 to add drug prescription "
        "\n     3 to add lab test prescription "
        "\n     4 to view sickness details "
        "\n     5 to view previous drug prescriptions "
        "\n     6 to view lab test prescription "
        "\n     7 to edit account "
        "\n     8 to renew password "
        "\n     9 to view account"
        "\n     -1 to exit\n ")

    while True:
        option = input()
        if option in ['1', '2', '3', '4', '5', '6']:
            while True:
                patient_id = input("Enter patient id: ")
                if check_existing_patients(patient_id):
                    break
                else:
                    print("Invalid patient id")
            if option == '1':
                Doctor().update_sickness_details(patient_id)
            elif option == '2':
                Doctor().update_drug_prescription(patient_id)
            elif option == '3':
                Doctor().update_labtest_prescription(patient_id)
            elif option == '4':
                Doctor().display_sickness_details(patient_id)
            elif option == '5':
                Doctor().display_drug_prescription(patient_id)
            elif option == '6':
                Doctor().display_labtest_prescription(patient_id)
        elif option == '7':
            update_account(user_id)
        elif option == '8':
            renew_password(user_id)
        elif option == '9':
            view_account(user_id)
        elif option == '-1':
            print("Thank you Doctor")
            break
        else:
            print("Invalid input. Try again")


def handle_patient_actions(user_id):
    print(
        "Press  :"
        "\n     1 to change password "
        "\n     2 to update account "
        "\n     3 to view account details"
        "\n     4 to view sickness details "
        "\n     5 to view previous drug prescriptions "
        "\n     6 to view lab test prescription "
        "\n     -1 to exit\n ")

    while True:
        option = input()
        if option == '1':
            renew_password(user_id)
        elif option == '2':
            update_account(user_id)
        elif option == '3':
            view_account(user_id)
        elif option == '4':
            Patient().display_sickness_details(user_id)
        elif option == '5':
            Patient().read_drug_prescription(user_id)
        elif option == '6':
            Patient().read_labtest_prescription(user_id)
        elif option == '-1':
            print("Thank you")
            break
        else:
            print("Invalid input!")
