from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    try:
        send_mail(
            'Welcome!',
            'Thank you for registering.',
            'from@example.com',
            [email],
            fail_silently=False,
        )
        print(f"Email sent successfully to {email}")
    except Exception as e:
        print(f"Error while sending email: {e}")