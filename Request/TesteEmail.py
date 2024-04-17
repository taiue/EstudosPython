import smtplib
import email.message

def enviar_email():

    email_remetente = 'potatoe885@gmail.com'
    senha = '8726 4623'
    email_destinatario = 'taime885@gmail.com'
    assunto = 'teste'
    corpo_email = """ 
    <p> Paragrafo1 </p>
    <p> Paragrafo2 </p>
      """
#construão smtp e corpo email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_remetente, senha)

    msg = email.message.Message()
    msg['Subbject'] = assunto
    msg['From'] = email_remetente
    msg['To'] = email_destinatario
    msg.add_header('Content_Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], senha)
    s.sendmail(msg['From'], msg.as_string().encode('utf-8'))
    print('email enviado')