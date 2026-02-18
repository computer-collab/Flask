from  werkzeug.security import *
def HashGen(Password):
    return generate_password_hash(Password)

def VerifyCredentials(Password_Hashed=None,Password_Original=None):
    if Password_Hashed and Password_Original:
        return check_password_hash(Password_Hashed,Password_Original)

    else :
       print("Empty credentials") 
       return 
    pass

if __name__ == "__main__":
    print(VerifyCredentials("x"))