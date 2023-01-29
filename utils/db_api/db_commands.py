from asgiref.sync import sync_to_async

from admin_panel.telebot.models import Users


@sync_to_async()
def create_user(telegram_id, username):
    return Users.objects.get_or_create(telegram_id=telegram_id, username=username)


@sync_to_async()
def select_user(telegram_id):
    return Users.objects.filter(telegram_id=telegram_id).first()

@sync_to_async()
def update_nickname(telegram_id, nickname):
    Users.objects.filter(telegram_id=telegram_id).update(nickname=nickname)

@sync_to_async()
def update_description(telegram_id, description):
    Users.objects.filter(telegram_id=telegram_id).update(description=description)

@sync_to_async()
def update_settings(telegram_id, setting):
    Users.objects.filter(telegram_id=telegram_id).update(settings=setting)