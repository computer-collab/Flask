from  werkzeug.security import *
from modules import GenerateOTP
def HashGen(Password):
    return generate_password_hash(Password)

def VerifyCredentials(Email,Password):
    pass

GenerateOTP("kummarirahul1980@gmail.com")


