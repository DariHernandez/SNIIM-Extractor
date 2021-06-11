import os
import log
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

current_dir = os.path.dirname(__file__)
current_file = os.path.basename(__file__)

class Email_manager (): 
    """Manage emails: connect and send mails
    """
    
    def __init__(self, email, password): 
        """Constrcutor of class
        """
        
        # Dictionary of server and post for smtp and imap protocol        
        servers_ports = {
            "gmail.com": {
                "smtp_server": "smtp.gmail.com",
                "smtp_port": 587,
                "imap_server": "imap.gmail.com",
                "imap_port": 993
            }, 
            "outlook.com": {
                "smtp_server": "smtp.office365.com",
                "smtp_port": 587,
                "imap_server": "outlook.office365.com",
                "imap_port": 993
            },
            "hotmail.com": {
                "smtp_server": "smtp.office365.com",
                "smtp_port": 587,
                "imap_server": "outlook.office365.com",
                "imap_port": 993
            },
            "live.com": {
                "smtp_server": "smtp.office365.com",
                "smtp_port": 587,
                "imap_server": "outlook.office365.com",
                "imap_port": 993
            },
            "yahoo.com": {
                "smtp_server": "smtp.mail.yahoo.com",
                "smtp_port": 587,
                "imap_server": "imap.mail.yahoo.com",
                "imap_port": 993
            }, 
            "aol.com": {
                "smtp_server": "smtp.aol.com",
                "smtp_port": 465,
                "imap_server": "imap.aol.com",
                "imap_port": 993
            }
        }
        
        # Credentials
        self.email = email
        self.password = password
        
        # Get correct server and port
        email_domain = self.email[self.email.find("@")+1:]
        self.smtp_server = servers_ports[email_domain]["smtp_server"]
        self.smtp_port = servers_ports[email_domain]["smtp_port"]
        self.imap_server = servers_ports[email_domain]["imap_server"]
        self.imap_port = servers_ports[email_domain]["imap_port"]
        
        
    def __connect_smtp (self): 
        """Connect to smtp server for the email
        """
        
        message = "Connecting to smtp..."
        log.info(message, current_file)
        
        # Connect to server and port
        self.smtpObj = smtplib.SMTP (self.smtp_server, self.smtp_port)

        # Send hello to smtp
        self.smtpObj.ehlo()

        # Active encriptation
        self.smtpObj.starttls()

        # login
        self.smtpObj.login (self.email, self.password)
        
        message = "Connected to smtp"
        log.info(message, current_file)
    
    def send_email (self, receivers=[], subject="", body="", files=[]): 
        """Send email to specific receivers
        """
        
        self.__connect_smtp()
        
        # Create text menssage
        menssage = f"Subject: {subject}\n\n{body}"
        
        # Send emails
        for receiver in receivers: 
                        
            # Make an instance of mime multipart to create the message
            message = MIMEMultipart()

            # Add main part to the email
            message['From'] = self.email
            message["To"] = receiver
            message["Date"] = formatdate(localtime=True)
            message["Subject"] = subject

            # Add tex5t to the email
            text = body

            message.attach (MIMEText(text))

            # Loop for files in list
            for file in files:

                # Read file and create email part 
                file_binary = open(file, "rb")
                part = MIMEApplication(file_binary.read(), name=os.path.basename(file))
                file_binary.close()

                # Add file to the message
                part['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(file))
                message.attach(part)

            # Send email
            self.smtpObj.sendmail(self.email, 
                            receiver, 
                            message.as_string())

        # Close connection
        self.smtpObj.quit()
