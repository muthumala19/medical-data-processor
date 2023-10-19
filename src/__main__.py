from src.auth.signup import SignUp
from src.app import main

if __name__ == '__main__':
    choice = input("Press 1 to sign in or 2 to sign up: ")
    if choice == '1':
        main()
    elif choice == '2':
        SignUp().create_user()
        print("Sign In to your account")
        main()
    else:
        print("Authentication failed")
