from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import ssl

def send_email():
        
    # Define these once; use them twice!
    strFrom = 's.p@castsoftware.com'
    strTo = 's.mahton@castsoftware.com'
    HOST = 'email-smtp.eu-central-1.amazonaws.com'
    PORT = 587
    USERNAME_SMTP = 'AKIAZV4FQR23NGDUIIOI'
    PASSWORD_SMTP = 'BNcNAA8oGY2cl2VRwufb8hgRyAScUVxc0S6e8c1Z+ewP'


    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'test message'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    # This example assumes the image is in the current directory
    with open('img\logo.png', 'rb') as fp:
        msgImage = MIMEImage(fp.read())
    
    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    with open('ApplicationHealth.htm', 'r') as myfile:
        data=myfile.read()

    msgHTML = MIMEText(data, 'html')
    msgAlternative.attach(msgHTML)

    # Try to send the message.
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(HOST, PORT) as server:
            server.starttls(context=context)
            server.login(USERNAME_SMTP, PASSWORD_SMTP)
            server.sendmail(strFrom, strTo, msgRoot.as_string())
            server.close()
            print("Email sent!")

    except smtplib.SMTPException as e:
        print("Error: ", e)
