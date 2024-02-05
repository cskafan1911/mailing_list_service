from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Users(AbstractUser):
    """
    Класс модели пользователей.
    """

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    first_name = models.CharField(max_length=100, verbose_name='Имя пользователя', **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия пользователя', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='user_avatar', verbose_name='аватар', **NULLABLE)
    email_verify = models.BooleanField(default=False)
    company = models.CharField(max_length=45, verbose_name='Компания', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """
        Строковое представление модели Users.
        :return: Почта пользователя.
        """
        return f'{self.first_name} {self.last_name} ({self.email})'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = (
            ('user_moderator_perm', 'модератор'),
                       )
