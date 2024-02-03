from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Mailing(models.Model):
    """
    Класс модели рассылки.
    """

    HOUR = 'HOUR'
    WEEK = 'WEEK'
    MONTH = 'MONTH'
    FREQUENCY_CHOICES = [
        (HOUR, 'раз в час'),
        (WEEK, 'раз в неделю'),
        (MONTH, 'раз в месяц'),
    ]

    COMPLETED = 'COMPLETED'
    CREATED = 'CREATED'
    LAUNCHED = 'LAUNCHED'
    STATUS_CHOICES = [
        (COMPLETED, 'завершена'),
        (CREATED, 'создана'),
        (LAUNCHED, 'запущена'),
    ]

    user_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Рассылка пользователя', **NULLABLE)

    name = models.CharField(max_length=50, verbose_name='Наименование рассылки', **NULLABLE)
    time_start = models.DateTimeField(verbose_name='Время начала')
    time_stop = models.DateTimeField(verbose_name='Время окончания')
    frequency = models.CharField(max_length=5, choices=FREQUENCY_CHOICES, default=WEEK,
                                 verbose_name='Периодичность рассылки')
    status_mailing = models.CharField(max_length=10, choices=STATUS_CHOICES, default=COMPLETED,
                                      verbose_name='Статус рассылки')

    def __str__(self):
        """
        Строковое представление рассылки
        :return: Имя пользователя, имя рассылки, статус рассылки, периодичность рассылки
        """
        return f'{self.user_creator} - {self.name} ({self.status_mailing} - {self.frequency})'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    """
    Класс модели сообщения для рассылки.
    """

    subject = models.CharField(max_length=100, verbose_name='Тема письма')
    message = models.TextField(verbose_name='Тело письма')
    message_for_mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Сообщение рассылки')

    def __str__(self):
        """
        Строкове представление модели Message.
        """
        return f'Сообщение {self.subject} для рассылки {self.message_for_mailing}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

