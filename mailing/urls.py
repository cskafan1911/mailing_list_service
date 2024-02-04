from django.contrib.auth.views import LoginView
from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingCreateView, MailingListView, MailingUpdateView, MailingDetailView, MailingDeleteView, \
    start_mailing, stop_mailing

app_name = MailingConfig.name

urlpatterns = [
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
    path('update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('<int:pk>/detail/', MailingDetailView.as_view(), name='mailing_detail'),
    path('start_mailing/<int:pk>', start_mailing, name='start_mailing'),
    path('stop_mailing/<int:pk>', stop_mailing, name='stop_mailing'),

]
