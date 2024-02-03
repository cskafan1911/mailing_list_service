from django.shortcuts import render
from django.views.generic import TemplateView

from mailing.models import Mailing


class IndexView(TemplateView):
    """
    Класс для отображения главной страницы.
    """

    template_name = 'main/index.html'
    extra_context = {
        'title': 'Список наших рассылок'
    }

    def get_context_data(self, **kwargs):
        pass
        """
        Метод для получения рассылок.
        """
        context_data = super(IndexView, self).get_context_data(**kwargs)
        context_data['object_list'] = Mailing.objects.all()

        return context_data

# def index(request):
#     """
#     Отображение главной страницы
#     """
#     return render(request, 'main/index.html')
