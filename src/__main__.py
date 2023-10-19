from src.auth.signup import SignUp
from src.main import main

def app():
    choice = input("Enter :"
                   "\n      1 to signin"
                   "\n      2 to signup"
                   "\n")
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
