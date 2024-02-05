
from django.shortcuts import render
from django.views.generic import TemplateView

from blog.models import Blog
from clients.models import Clients
from mailing.models import Mailing
from mailing.services import get_cache_objects_list


class IndexView(TemplateView):
    """
    Класс для отображения главной страницы.
    """

    template_name = 'main/index.html'
    extra_context = {
        'title': 'Список наших рассылок'
    }

    def get_context_data(self, **kwargs):
        """
        Метод для вывода на главный экран информации.
        """
        context_data = super(IndexView, self).get_context_data(**kwargs)
        context_data['mailings'] = len(Mailing.objects.all())
        context_data['active_mailings'] = len(Mailing.objects.filter(status_mailing='LAUNCHED'))
        context_data['clients'] = len(Clients.objects.all())
        context_data['blogs'] = get_cache_objects_list(Blog.objects.all())

        return context_data
