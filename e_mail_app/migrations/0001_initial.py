# Generated by Django 4.2 on 2024-04-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('first_name', models.CharField(max_length=10, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=10, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=20, null=True, verbose_name='Отчество')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
