from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Класс для настройки панели администратора модели Blog
    """

    list_display = ('pk', 'title', 'date_of_publication', 'view_count')
    list_filter = ('date_of_publication', 'view_count')
