# Generated by Django 4.2.7 on 2024-02-01 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('log', '0001_initial'),
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='mailing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='Рассылка'),
        ),
    ]
