from django.urls import path
from django.views.decorators.cache import cache_page

from main.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
