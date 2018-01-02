from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

class Notifier:
    @classmethod
    def notify(cls, email, password, courseURL):

        # create message
        msg = MIMEText('THERE IS AN OPEN SEAT IN THIS CLASS: \n\n' + str(courseURL), _charset='utf-8')
        msg['Subject'] = Header('OPEN SEAT ALERT', 'utf-8')
        msg['From'] = email
        msg['To'] = email

        # send it via gmail
        s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
        s.set_debuglevel(1)
        try:
            s.login(email, password)
            s.sendmail(msg['From'], msg['To'], msg.as_string())
        finally:
            s.quit()