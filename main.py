from imap_tools import MailBox, AND
from notificacao import *
from dotenv import load_dotenv
import os

load_dotenv()

login = os.getenv('login')
senha = os.getenv('senha')
entrada = 'https://mail.google.com/mail/u/0/#inbox'
autor = os.getenv('autor')


# Integrando código no email
email = MailBox('imap.gmail.com').login(login, senha)

# Listando emails
lista = email.fetch(AND(from_=autor, seen=False))

# Passando parâmetros
try:
    for msg in lista:
        notifica(autor, msg.subject, entrada)
except:
    print('ERRO')