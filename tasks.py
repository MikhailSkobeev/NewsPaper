
from celery import shared_task
from django.core.mail import EmailMultiAlternatives


@shared_task
def send_mail_for_sub_once(sub_username, sub_useremail, html_content):

    msg = EmailMultiAlternatives(
        subject=f'Здравствуй, {sub_username}! Новая статья в вашем разделе!',
        from_email='mishaskobeev@yandex.ru',
        to=[sub_useremail]
    )

    msg.attach_alternative(html_content, 'text/html')

    print()
    print(html_content)
    print()


@shared_task
def send_mail_every_week(sub_username, sub_useremail, html_content):

    msg = EmailMultiAlternatives(
        subject=f'Здравствуй, {sub_username}, новые статьи за прошлую неделю в вашем разделе!',
        from_email='mishaskobeev@yandex.ru',
        to=[sub_useremail]
    )

    msg.attach_alternative(html_content, 'text/html')
    print()

    print(html_content)
