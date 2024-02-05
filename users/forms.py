from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from mailing.forms import StyleFormMixin
from users.models import Users


class UsersRegisterForm(StyleFormMixin, UserCreationForm):
    """
    Класс для формы регистрации приложения Users.
    """

    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'phone', 'email', 'avatar', 'company', 'password1', 'password2')


class UsersProfileForm(StyleFormMixin, UserChangeForm):
    """
    Класс для формы просмотра профиля пользователя.
    """

    class Meta:
        model = Users
        fields = ('email', 'first_name', 'last_name', 'phone', 'email', 'avatar', 'company')
