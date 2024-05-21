from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from e_mail_app.models import NULLABLE


class User(AbstractUser):
    role_variants = (
        ('manager', 'Менеджер'),
        ('admin', 'Администратор')
    )
    username = None
    email = models.EmailField(unique=True, verbose_name='E-mail')

    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    country = models.CharField(max_length=25, verbose_name='Страна', **NULLABLE)
    is_verified = models.BooleanField(default=False, verbose_name='Подтверждён')
    token = models.CharField(max_length=10, verbose_name='Токен', **NULLABLE)
    role = models.CharField(max_length=20, default='manager', choices=role_variants,
                            verbose_name='Роль пользователя')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
