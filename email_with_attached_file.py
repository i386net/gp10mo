import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from    email import encoders


def send_attachment():
    from_address = ''  # от кого
    to_address = ''  # кому
    subject = ''  # тема письма
    login = ''  # логин на сервере
    password = ''  # пароль
    smtpserver = ''  # адрес smtp сервера

    message = MIMEMultipart()

    message['From'] = from_address
    message['To'] = to_address
    message['Subject'] = subject

    body = ''  # email text

    message.attach(MIMEText(body, 'plain'))

    file_name = ''  # file with ext

    with open(file_name) as attachment:
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= {}".format(file_name))
        message.attach(p)

    server = smtplib.SMTP(smtpserver)
    server.set_debuglevel(1)
    server.starttls()
    server.login(login, password)
    text = message.as_string()
    server.sendmail(from_address, to_address, text)
