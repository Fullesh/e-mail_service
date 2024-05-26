# Generated by Django 4.2 on 2024-05-25 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('e_mail_app', '0017_alter_mailingsettings_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailingmessage',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец письма'),
        ),
        migrations.AddField(
            model_name='mailingsettings',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец рассылки'),
        ),
    ]