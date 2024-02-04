import datetime

import pytz
from django.conf import settings
from django.core.mail import send_mail

from clients.models import Clients
from log.models import Log
from mailing.models import Mailing, Message


def send_email(mailing):
    """
    Функция для создания и отправки сообщения.
    """
    if check_date_mailing(mailing):
        mailing = Mailing.objects.get(pk=mailing.pk)
        message = Message.objects.get(message_for_mailing=mailing.pk)
        clients = Clients.objects.filter(mailing=mailing.pk)
        logs = []
        success_answer = 0
        unsuccessful_answer = 0
        for client in clients:
            try:
                send_mail(
                    subject=message.subject,
                    message=message.message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email]
                )
                logs.append(
                    f'Рассылка: {mailing.name}, Дата: {datetime.datetime.now()}, Клиент: {client.email}---Успешно')
                success_answer += 1
            except Exception:
                logs.append(
                    f'Рассылка: {mailing.name}, Дата: {datetime.datetime.now()}, Клиент: {client.email}---Ошибка')
                unsuccessful_answer += 1
            save_log_of_mailing(mailing, logs, success_answer, unsuccessful_answer)
            change_datetime_mailing(mailing)
    else:
        mailing.status_mailing = 'COMPLETED'
        mailing.save()


def change_datetime_mailing(mailing):
    """
    После отправки рассылки, меняет дату отправки в соответствии с периодичностью отправки.
    """
    if mailing.frequency == 'HOUR':
        mailing.time_start = datetime.datetime.now() + datetime.timedelta(hours=1)
    elif mailing.frequency == 'WEEK':
        mailing.time_start = datetime.datetime.now() + datetime.timedelta(days=7)
    elif mailing.frequency == 'MONTH':
        mailing.time_start = datetime.datetime.now() + datetime.timedelta(days=30)
    mailing.save()


def check_date_mailing(mailing):
    """
    Проверка даты и времени рассылки.
    """
    utc = pytz.UTC
    now = datetime.datetime.now().replace(tzinfo=utc)
    if mailing.time_stop > now:
        return True

    return False


def check_status_mailing(mailing):
    """
    Проверка статуса рассылки.
    """
    if mailing.status_mailing != 'COMPLETED':
        if len(Message.objects.filter(message_for_mailing=mailing.pk).all()) > 0 and len(
                Message.objects.filter(message_for_mailing=mailing.pk).all()) > 0:
            return 'LAUNCHED'
        return 'CREATED'

    else:
        return 'COMPLETED'


def send_mailings():
    """
    Функция для отправки готовых рассылок.
    """
    utc = pytz.UTC
    now = datetime.datetime.now().replace(tzinfo=utc)
    mailings = Mailing.objects.filter(status_mailing='LAUNCHED').all()
    count_mailings = 0
    for mailing in mailings:
        datetime_mailing_start = mailing.time_start.replace(tzinfo=utc)
        if now > datetime_mailing_start:
            if check_date_mailing(mailing):
                send_email(mailing)
                count_mailings += 1
        else:
            mailing.status_mailing = 'COMPLETED'
            mailing.save()
    if count_mailings > 0:
        print(f'Отправлено всего: {count_mailings}')
    else:
        print(f'Рассылок для отправки пока нет.')


def save_log_of_mailing(mailing, logs, success_answer, unsuccessful_answer):
    """
    Функция сохраняет логи рассылки.
    """
    new_log = {
        "last_datetime": datetime.datetime.now(),
        "mailing": mailing,
        "attempt_status": f"Успешно - {success_answer}, Ошибка - {unsuccessful_answer}",
        "mail_server_response": logs,
    }

    Log.objects.create(**new_log)
