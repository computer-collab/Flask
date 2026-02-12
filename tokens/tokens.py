import json
def VerifyToken(tokenx):
    with open('token.json', 'r', encoding='utf-8') as file:
        
        token = json.load(file)
        print(token)
        if str(token) ==  str(tokenx):
            return True
        else :
            return False
        
if __name__ == "__main__":
    VerifyToken("12345678")