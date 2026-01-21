from  werkzeug.security import generate_password_hash, check_password_hash
from otp import GenerateOTP
def HashGen(Password):
    return generate_password_hash(Password)

def VerifyCredentials(Email,Password):
    pass
print(GenerateOTP(input("enter email")))

