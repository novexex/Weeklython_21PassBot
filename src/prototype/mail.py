import smtplib
from email.mime.text import MIMEText

def send_email(message):
    sender = "21passbot@gmail.com"
    password = "rgvbephtmlysitga"
    receiver = "ieshachr@student.21-school.ru"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Твой код подтверждения для school21pass_bot"
        server.sendmail(sender, receiver, msg.as_string())

        return "The message was send succsesfully"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password, and try again"

def main():
    message = input("Type your message: ")
    print(send_email(message=message))

if __name__ == "__main__":
    main()
