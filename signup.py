from  werkzeug.security import *
from otp import GenerateOTP
def HashGen(Password):
    return generate_password_hash(Password)

def VerifyCredentials(Email,Password):
    pass
#print(GenerateOTP(input("enter email")))

