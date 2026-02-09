import json,os
def VerifyToken(intoken):
    with open('./tokens/token.json', 'r', encoding='utf-8') as file:
        
        token = json.load(file)
        if str(intoken) in token.get("token"):
            return True
        else :
            return False
        
print(os.getcwd())
print(VerifyToken("rahulxyz"))