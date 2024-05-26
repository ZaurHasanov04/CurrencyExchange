from django.conf import settings
from django.core.mail import send_mail


def send_otp(email, otp):
    message = f'Your acctivation code id {otp}'
    subject = 'Activation Code'
    from_email = settings.EMAIL_HOST_USER
    to_email = [email]

    send_mail(subject, message, from_email, to_email)
