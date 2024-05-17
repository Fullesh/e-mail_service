import pytz
from datetime import timedelta, datetime
from config import settings
from django.core.mail import send_mail

from e_mail_app.models import MailingSettings, MailingMessage, Client, Logger


def my_job():
    day = timedelta(days=1)
    week = timedelta(days=7)
    month = timedelta(days=31)

    zone = pytz.timezone(settings.TIME_ZONE)
    today = datetime.now(zone)
    mailings = MailingSettings.objects.all().filter(is_active=True)

    for mailing in mailings:
        if mailing.status != 'finished':
            mailing.status = 'executing'
            mailing.save()
            emails_list = [client.email for client in mailing.client.all()]

            print(f'Рассылка {mailing.id} - начало {mailing.start_time}; конец {mailing.end_time}')

            result = send_mail(
                subject=mailing.mail.subject,
                message=mailing.mail.message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=emails_list
            )
            print('Пошла рассылОчка')

            status = result == True

            log = Logger(mailing=mailing, status=status)
            log.save()

            if mailing.period == 'per_day':
                mailing.next_date = log.last_time_sending + day
            elif mailing.period == 'per_week':
                mailing.next_date = log.last_time_sending + week
            elif mailing.period == 'per_month':
                mailing.next_date = log.last_time_sending + month

            if status:  # на случай сбоя рассылки она останется активной
                if mailing.next_date < mailing.end_time:
                    mailing.status = 'created'
                else:
                    mailing.status = 'finished'

            mailing.save()
            print(f'Рассылка {mailing.client.first_name} отправлена {today} (должна была {mailing.next_date})')
