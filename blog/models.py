from django.db import models

from users.models import NULLABLE


class Blog(models.Model):
    """
    Класс для блога.
    """

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog_image', **NULLABLE, verbose_name='Изображение')
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    date_of_publication = models.DateTimeField(auto_now_add=True, **NULLABLE, verbose_name='Дата публикации')

    def __str__(self):
        """
        Строковое представление модели Blog.
        """
        return f'Статья {self.title} (просмотров: {self.view_count})'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        permissions = (
            ('blog_custom_perm', 'модератор блога'),
        )
