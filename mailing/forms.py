from django import forms

from mailing.models import Mailing, Message


class StyleFormMixin:
    """
    Класс Mixin для стилизации форм.
    """

    def __init__(self, *args, **kwargs):
        """
        Инициализация класса StyleFormMixin.
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):
    """
    Класс для форм объекта Mailing.
    """

    class Meta:
        model = Mailing
        exclude = ('user_creator',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    """
    Класс для форм объекта Mailing.
    """

    class Meta:
        model = Message
        exclude = ('message_for_mailing',)
