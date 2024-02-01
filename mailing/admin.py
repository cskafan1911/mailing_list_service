from django.contrib import admin

from mailing.models import Mailing, Message


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    """
    Класс для настройки панели администратора модели Clients.
    """

    list_display = ('user', 'name', 'time_start', 'time_stop', 'frequency', 'status_mailing')
    list_filter = ('user', 'status_mailing', 'frequency')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Класс для настройки панели администратора модели Message.
    """

    list_display = ('message_for_mailing', 'subject')
    list_filter = ('subject',)
