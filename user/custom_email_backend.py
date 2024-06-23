import certifi,smtplib
import ssl
from django.core.mail.backends.smtp import EmailBackend

class CustomEmailBackend(EmailBackend):
    def open(self):
        if self.connection:
            return False
        try:
            self.connection = smtplib.SMTP(self.host,self.port)
            self.connection.ehlo()
            self.connection.starttls(context=ssl._create_unverified_context())
            self.connection.ehlo()
            if self.username and self.password:
                self.connection.login(self.username,self.password)
            return True
        except :
            if not self.fail_silently:
                raise
            return False

    # def _create_connection(self):
    #     return super()._create_connection()