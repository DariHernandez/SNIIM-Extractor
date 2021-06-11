import os
import config
import log
import globals
from email_manager.sender import Email_manager

def send_file ():
    """Send xlsx file from email receivers 
    """

    # Get credentials
    email = config.get_credential("email")
    password = config.get_credential("password")
    to_email = config.get_credential("to_email")

    # Send email with file
    log.update_status(f"Accediendo al email: \n{email}")
    
    xlsx_file = os.path.join(os.path.dirname(__file__), "resultados.xlsx")
    text = "Archivo de SNIIM"
    email = Email_manager(email, password)
    
    log.update_status(f"Enviando correo a: \n{to_email}")
    
    if globals.loading:
        email.send_email([to_email], subject=text, body=text, files=[xlsx_file])
    
    log.update_status(f"Correo enviado a: \n{to_email}.")