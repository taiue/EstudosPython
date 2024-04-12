from flask import Flask, request, jsonify
import requests
import json
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
CORS(app)

@app.route('/enviar_email', methods=['POST'])
def enviar_email():
    data = request.get_json()

    email_remetente = data['potatoe885@gmail.com']
    senha_remetente = data['Potatoe@123']

    email_destinatario = data['taime885@gmail.com']
    assunto = data['teste']
    mensagem = data['teste']

    try:
        # Configurar servidor SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_remetente, senha_remetente)

        # Construir o email
        msg = MIMEMultipart()
        msg['De'] = email_remetente
        msg['Para'] = email_destinatario
        msg['Assunto'] = assunto
        msg.attach(MIMEText(mensagem, 'plain'))

        # Enviar email
        server.sendmail(email_remetente, email_destinatario, msg.as_string())
        server.quit()

        return jsonify({'message': 'Email enviado com sucesso!'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)