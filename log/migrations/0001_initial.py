# Generated by Django 4.2.7 on 2024-02-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_datetime', models.DateTimeField(verbose_name='Последняя рассылка')),
                ('attempt_status', models.CharField(max_length=100, verbose_name='Статус попытки')),
                ('mail_server_response', models.CharField(max_length=300, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Лог рассылки',
                'verbose_name_plural': 'Логи рассылки',
            },
        ),
    ]
