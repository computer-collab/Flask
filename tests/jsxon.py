import json
with open('token.json', 'r', encoding='utf-8') as file:
    
    token = json.load(file)
    print(token.get('token'))  # Yeh ek string return karega
    