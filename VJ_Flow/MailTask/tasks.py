from celery import shared_task
from django.core.mail import send_mail

@shared_task
def SendMail(email):
    send_mail(
        subject="Scheduler Sample Mail",
        message="Hello this is a sample mail from celery scheduler to check whether it works well or not",
        from_email='connectly.now@gmail.com',
        recipient_list=[email],
    )
    print(f"Sent reminder email to {email}")