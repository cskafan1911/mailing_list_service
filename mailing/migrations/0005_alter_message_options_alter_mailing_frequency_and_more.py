# Generated by Django 4.2.7 on 2024-02-03 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_alter_mailing_user_creator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterField(
            model_name='mailing',
            name='frequency',
            field=models.CharField(choices=[('Раз в час', 'раз в час'), ('Раз в неделю', 'раз в неделю'), ('Раз в месяц', 'раз в месяц')], default='Раз в неделю', max_length=12, verbose_name='Периодичность рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='status_mailing',
            field=models.CharField(choices=[('Завершена', 'завершена'), ('Создана', 'создана'), ('Запущена', 'запущена')], default='Завершена', max_length=10, verbose_name='Статус рассылки'),
        ),
    ]
