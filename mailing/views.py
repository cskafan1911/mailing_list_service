import pytz
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from clients.forms import ClientsForm
from clients.models import Clients
from log.models import Log
from mailing.forms import MailingForm, MessageForm
from mailing.models import Mailing, Message
from mailing.services import check_status_mailing, send_email, send_mailings
from users.models import Users


class MailingListView(ListView):
    """
    Класс для вывода списка рассылок пользователя.
    """
    model = Mailing
    permission_required = 'users.user_moderator_perm'

    def get_queryset(self):
        """
        Метод получает список рассылок пользователя.
        """
        queryset = super().get_queryset()
        if self.request.user.has_perm('users.user_moderator_perm'):
            return queryset
        else:
            queryset = queryset.filter(user_creator=self.request.user)

        return queryset


class MailingCreateView(LoginRequiredMixin, CreateView):
    """
    Класс для создания рассылки.
    """

    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('index')
    extra_context = {
        'title': 'Введите информацию о рассылке',
    }

    def form_valid(self, form):
        """
        Метод объединяет пользователя и созданный им объект модели Mailing.
        """

        self.object = form.save()
        self.object.user_creator = self.request.user
        self.object.save()

        context_data = self.get_context_data()
        MessageFormset = context_data['message_formset']
        ClientsFormset = context_data['clients_formset']
        self.object = form.save()
        self.object.user_creator = self.request.user

        if MessageFormset.is_valid() and ClientsFormset.is_valid():
            MessageFormset.instance = self.object
            MessageFormset.save()
            ClientsFormset.instance = self.object
            ClientsFormset.save()
            self.object.status_mailing = check_status_mailing(self.object)
        else:
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Метод связывает рассылку, клиента и сообщение.
        """
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(Mailing, Message, form=MessageForm, extra=1)
        ClientsFormset = inlineformset_factory(Mailing, Clients, form=ClientsForm, extra=1)
        if self.request.method == 'POST':
            context_data['message_formset'] = MessageFormset(self.request.POST, instance=self.object)
            context_data['clients_formset'] = ClientsFormset(self.request.POST, instance=self.object)
        else:
            context_data['message_formset'] = MessageFormset(instance=self.object)
            context_data['clients_formset'] = ClientsFormset(instance=self.object)

        return context_data


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    """
    Класс для редактирования рассылки.
    """

    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        Метод объединяет пользователя и созданный им объект модели Mailing.
        """

        self.object = form.save()
        self.object.user_creator = self.request.user
        self.object.save()

        context_data = self.get_context_data()
        MessageFormset = context_data['message_formset']
        ClientsFormset = context_data['clients_formset']
        self.object = form.save()
        self.object.user_creator = self.request.user
        if MessageFormset.is_valid() and ClientsFormset.is_valid():
            MessageFormset.instance = self.object
            MessageFormset.save()
            ClientsFormset.instance = self.object
            ClientsFormset.save()
            self.object.status_mailing = check_status_mailing(self.object)
        else:
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Метод связывает рассылку, клиента и сообщение.
        """
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(Mailing, Message, form=MessageForm, extra=1)
        ClientsFormset = inlineformset_factory(Mailing, Clients, form=ClientsForm, extra=1)
        if self.request.method == 'POST':
            context_data['message_formset'] = MessageFormset(self.request.POST, instance=self.object)
            context_data['clients_formset'] = ClientsFormset(self.request.POST, instance=self.object)
        else:
            context_data['message_formset'] = MessageFormset(instance=self.object)
            context_data['clients_formset'] = ClientsFormset(instance=self.object)

        return context_data

    def get_object(self, queryset=None):
        """
        Метод проверяет, может ли пользователь редактировать объект модели Products.
        """
        self.object = super().get_object()
        if self.object.user_creator != self.request.user:
            raise Http404('Вы можете смотреть и редактировать только свои рассылки!')

        return self.object


class MailingDetailView(DetailView):
    """
    Класс для отображения информации о рассылке.
    """

    model = Mailing
    permission_required = 'users.user_moderator_perm'

    def get_context_data(self, **kwargs):
        """
        Метод добавляет сообщение в рассылку.
        """

        context_data = super().get_context_data(**kwargs)
        context_data['message'] = Message.objects.filter(message_for_mailing=self.object).last()
        context_data['clients'] = Clients.objects.filter(mailing=self.object).all()
        context_data['logs'] = Log.objects.filter(mailing=self.object).all()

        return context_data

    def get_object(self, queryset=None):
        """
        Метод проверяет, может ли пользователь редактировать объект модели Products.
        """
        self.object = super().get_object()
        if self.request.user.has_perm('users.user_moderator_perm'):
            return self.object
        elif self.object.user_creator != self.request.user:
            raise Http404('Вы можете смотреть и редактировать только свои рассылки!')

        return self.object


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    """
    Класс для удаления рассылок.
    """

    model = Mailing
    success_url = reverse_lazy('index')
    permission_required = 'users.user_moderator_perm'

    def get_object(self, queryset=None):
        """
        Метод проверяет, может ли пользователь редактировать объект модели Products.
        """
        self.object = super().get_object()
        if self.object.user_creator != self.request.user:
            raise Http404('Вы можете смотреть и редактировать только свои рассылки!')

        return self.object


def start_mailing(request, pk):
    """
    Функция запускает рассылку.
    """
    mailing = Mailing.objects.get(pk=pk)
    if mailing.user_creator == request.user:
        send_email(mailing)
        return redirect(request.META.get('HTTP_REFERER'))
    raise Http404


def stop_mailing(request, pk):
    """
    Функция отключает рассылку.
    """
    mailing = Mailing.objects.get(pk=pk)
    if mailing.user_creator == request.user or request.user.has_perm('users.user_moderator_perm'):
        mailing.status = 'COMPLETED'
        mailing.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        raise Http404
