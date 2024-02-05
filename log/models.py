from django.db import models

from mailing.models import Mailing


class Log(models.Model):
    """
    Класс модели Log
    """

    last_datetime = models.DateTimeField(verbose_name='Последняя рассылка')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    attempt_status = models.CharField(max_length=100, verbose_name='Статус попытки')
    mail_server_response = models.CharField(max_length=300, verbose_name='Ответ')

    def __str__(self):
        """
        Строковое представление класса Log
        :return: Время, статус попытки, ответ почтового сервиса
        """
        return f'{self.last_datetime}: {self.attempt_status}, {self.mail_server_response}'

    class Meta:
        verbose_name = 'Лог рассылки'
        verbose_name_plural = 'Логи рассылки'
