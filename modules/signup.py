from  werkzeug.security import *
def HashGen(Password):
    return generate_password_hash(Password)

def VerifyCredentials(Email,Password):
    pass

