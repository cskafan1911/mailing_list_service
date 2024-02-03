from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, TemplateView, UpdateView

from users.forms import UsersRegisterForm, UsersProfileForm
from users.models import Users


class RegisterView(CreateView):
    """
    Класс для регистрации пользователя.
    """

    model = Users
    form_class = UsersRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """
        Метод для проверки валидации почты пользователя.
        Генерирует ссылку для валидации и отправляет на электронную почту пользователя.
        """
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_url = reverse_lazy('users:confirm_email', kwargs={'uidb64': uid, 'token': token})
        current_site = get_current_site(self.request)
        send_mail(
            'Подтвердите электронный адрес',
            f'Ссылка для подтверждения: http://{current_site.domain}{activation_url}',
            settings.EMAIL_HOST_USER,
            [user.email]
        )
        return redirect('users:email_confirmation_sent')


class UserConfirmEmailView(View):
    """
    Класс активации пользователя, после проверки электронной почты.
    """

    @staticmethod
    def get(request, uidb64, token):
        """
        Метод сравнивает сгенерированный код для проверки электронной почты и активирует пользователя
        после успешной проверки.
        """
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = Users.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.email_verify = True
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('users:email_confirmed')
        return redirect('users:email_confirmation_failed')


class EmailConfirmationSentView(TemplateView):
    template_name = 'users/email_confirmation_sent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Письмо активации отправлено'
        return context


class EmailConfirmedView(TemplateView):
    template_name = 'users/email_confirmed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваша почта активирована'
        return context


class EmailConfirmationFailedView(TemplateView):
    template_name = 'users/email_confirmation_failed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваша почта не активирована'
        return context


class ProfileView(UpdateView):
    model = Users
    form_class = UsersProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
