# Generated by Django 4.2 on 2024-05-03 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_mail_app', '0005_alter_mailingmessage_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailingsettings',
            name='mail',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='e_mail_app.mailingmessage'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mailingsettings',
            name='period',
            field=models.DateTimeField(choices=[('per_day', 'раз в день'), ('per_week', 'раз в неделю'), ('per_month', 'раз в месяц')], default='per_month', max_length=12, verbose_name='Периодичность рассылки'),
        ),
        migrations.AlterField(
            model_name='mailingsettings',
            name='status',
            field=models.CharField(choices=[('created', 'создана'), ('executing', 'запущена'), ('finished', 'закончена успешно'), ('error', 'законечена с ошибками')], default='created', max_length=15, verbose_name='Статус рассылки'),
        ),
    ]
