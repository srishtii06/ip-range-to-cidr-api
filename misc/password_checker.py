import bcrypt

def hash_password(password: str) -> str:
    """
    Hash a plain password using bcrypt
    """
    # Convert password to bytes
    password_bytes = password.encode('utf-8')
    
    # Generate random salt
    salt = bcrypt.gensalt()  # default rounds=12
    
    # Hash the password
    hashed = bcrypt.hashpw(password_bytes, salt)
    
    # Return hashed password as string
    return hashed.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password
    """
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


password = "abracadabra"

# Hash password
hashed_pw = hash_password(password)
print("Hashed:", hashed_pw)

# Verify password
is_valid = verify_password("abracadabra", hashed_pw)
print("Valid?", is_valid)  # True
