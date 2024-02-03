from django.contrib.auth.views import LoginView
from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingCreateView, MailingListView, MailingUpdateView, MailingDetailView, MailingDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('<int:pk>/', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailing/<int:pk>/detail/', MailingDetailView.as_view(), name='mailing_detail'),

]
