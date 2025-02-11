import getpass

def secure_password_input():
    """Securely takes a password input without displaying it."""
    password = getpass.getpass("Enter your password: ")
    print("Password received securely!")

if __name__ == "__main__":
    secure_password_input()
