from django.conf import settings
from django.db import models

from mailing.models import Mailing
from users.models import NULLABLE


class Clients(models.Model):
    """
    Класс модели клиентов
    """

    email = models.EmailField(verbose_name='почта')
    first_name = models.CharField(max_length=100, verbose_name='Имя клиента', **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия клиента', **NULLABLE)
    comment = models.CharField(max_length=300, verbose_name='Комментарий клиента', **NULLABLE)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления', **NULLABLE)

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE,
                                verbose_name='Рассылка')

    def __str__(self):
        """
        Строковое представление клиента.
        :return: Данные о клиенте
        """
        return f'Клиент пользователя: {self.mailing} - {self.first_name} {self.last_name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
