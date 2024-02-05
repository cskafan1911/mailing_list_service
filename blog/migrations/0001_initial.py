# Generated by Django 4.2.7 on 2024-02-03 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_image', verbose_name='Изображение')),
                ('view_count', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('date_of_publication', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
