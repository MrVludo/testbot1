from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# python django_app.py makemigrations
# python django_app.py migrate

class CreateModel(models.Model):
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    updated = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    class Meta:
        abstract = True


class Users(CreateModel):
    telegram_id = models.BigIntegerField(
        help_text='Telegram ID пользователя',
        verbose_name='Telegram ID'
    )

    username = models.CharField(
        max_length=200,
        null=True,
        help_text='Юзернейм пользователя',
        verbose_name='Юзернейм'
    )

    nickname = models.CharField(
        max_length=30,
        null=True,
        help_text="Придуманый никнейм пользователя",
        verbose_name="Никнейм"
    )

    description = models.CharField(
        max_length=100,
        null=True,
        help_text="Придуманное описание пользователя",
        verbose_name="Описание"
    )

    settings = models.BooleanField(
        default=True,
        help_text="Настройки пользователя (показывать / не показывать) свои мемы другим",
        verbose_name="настройки"
    )

    memes = models.CharField(
        max_length=10000,
        null=True,
        help_text="Список всех мемов пользователя",
        verbose_name="мемы"
    )


class Memes(models.Model):
    photo_id = models.CharField(
        max_length=10000,
        null=True,
        help_text='ID Фотографии',
        verbose_name='ID Фотографии'
    )

    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='user_id',
        blank=True,
        null=True,
        help_text='Пользователь',
        verbose_name='Пользователь'
    )


class Favorites(models.Model):
    photo_id = models.CharField(
        max_length=10000,
        null=True,
        help_text='ID Фотографии',
        verbose_name='ID Фотографии'
    )

    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='user_id_favorites',
        blank=True,
        null=True,
        help_text='Пользователь',
        verbose_name='Пользователь'
    )

