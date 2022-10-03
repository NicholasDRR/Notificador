from imap_tools import MailBox, AND
from notificacao import *
from dotenv import load_dotenv
import os

load_dotenv()

login = os.getenv('login')
senha = os.getenv('senha')
autor = os.getenv('autor')
entrada = 'https://mail.google.com/mail/u/0/#inbox'


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