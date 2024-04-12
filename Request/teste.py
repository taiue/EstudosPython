import requests
import json
# URL da sua API
url = 'http://localhost:5000/enviar_email'

# Dados do email
data = {
    "email": "potatoe885@gmail.com",
    "password": "Potatoe@123",
    "to_email": "taime885@example.com",
    "subject": "Assunto do Email",
    "message": "Corpo da mensagem."
}

# Converter os dados para JSON
payload = json.dumps(data)

# Configurar o cabeçalho
headers = {'Content-Type': 'application/json'}

# Enviar a solicitação POST
response = requests.post(url, headers=headers, data=payload)

# Verificar o código de status da resposta
print(response.status_code)
print(response.json())
