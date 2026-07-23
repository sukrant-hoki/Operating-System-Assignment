# Simple user database
USERS = {
    "admin": "admin123",
    "student": "student123"
}


def login():
    """
    Authenticates a user.
    Returns True if login is successful.
    """

    print("\n========== LOGIN ==========")

    username = input("Username: ")
    password = input("Password: ")

    if username in USERS and USERS[username] == password:
        print("\nLogin Successful!\n")
        return True

    print("\nInvalid username or password.\n")
    return False