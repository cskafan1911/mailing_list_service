from django.contrib import admin

from clients.models import Clients


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    """
    Класс для настройки панели администратора модели Clients.
    """

    list_display = ('email', 'first_name', 'last_name', 'mailing')
    list_filter = ('mailing',)
