from django.core.management import BaseCommand

from users.models import Users


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = Users.objects.create(
            email='admin@skypro.ru',
            first_name='Dmitry',
            last_name='Dronov',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('qwerty')
        user.save()
