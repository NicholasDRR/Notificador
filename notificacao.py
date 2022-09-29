import webbrowser
from win10toast_click import ToastNotifier

# Notificando
def open():
    try:
        webbrowser.open_new(useremail)
    except:
        print('ERRO')
        
# Configurando notificação
def notifica(autor, assunto, entrada):
    global useremail
    useremail = entrada
    notificar = ToastNotifier()
    notificar.show_toast( 
        autor,
        assunto,
        duration=10,
        threaded=True,
        callback_on_click=open
    )