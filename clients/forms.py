from django import forms

from clients.models import Clients
from mailing.forms import StyleFormMixin


class ClientsForm(StyleFormMixin, forms.ModelForm):
    """
    Класс для форм объекта Clients.
    """

    class Meta:
        model = Clients
        exclude = ('mailing',)