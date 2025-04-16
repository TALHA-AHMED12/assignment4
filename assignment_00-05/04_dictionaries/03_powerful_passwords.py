import hashlib

# Provided hash function (assuming it's already given)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Example stored logins (email -> hashed password)
stored_logins = {
    "user@example.com": "5e884898da28047151d0e56f8dc6292773603d0d9ea1e5b55eaaed6a058cf1c1",  # hash of "password"
    "admin@example.com": "6cb75f652a9b52798eb6cf2201057c73f5da9ed3445274ee5d07732e5b5b0ee7"   # hash of "12345"
}

def login(email, password_to_check):
    """
    Check if the provided password matches the stored hashed password for the given email.
    
    :param email: The email of the user trying to log in
    :param password_to_check: The password that the user is attempting to log in with
    :return: True if the passwords match, False otherwise
    """
    # Hash the input password and check it against the stored hashed password
    hashed_password = hash_password(password_to_check)
    
    if email in stored_logins:
        return stored_logins[email] == hashed_password
    else:
        return False

# Example usage:
email = input("Enter your email: ")
password = input("Enter your password: ")

if login(email, password):
    print("Login successful!")
else:
    print("Login failed. Invalid email or password.")
