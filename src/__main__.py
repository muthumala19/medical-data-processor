from src.auth.signup import SignUp
from src.app import main

def app():
    choice = input("Enter 1 to sign in or 2 to sign up: ")
    if choice == '1':
        main()
    elif choice == '2':
        SignUp().create_account()
        print("Sign Into your account")
        main()
    else:
        print("Authentication failed")


if __name__ == '__main__':
    app()
