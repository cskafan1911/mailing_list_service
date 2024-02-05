from django.core.management.base import BaseCommand
from mailing.services import send_mailings


class Command(BaseCommand):
    """
    Команда для отправки сообщений.
    """

    def handle(self, *args, **options):
        send_mailings()
