from asgiref.sync import sync_to_async

from admin_panel.telebot.models import Users, Memes, Favorites


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


@sync_to_async()
def create_row_memes(telegram_id, photo_id):
    user = Users.objects.filter(telegram_id=telegram_id).first()
    Memes.objects.get_or_create(user=user, photo_id=photo_id)


@sync_to_async()
def get_user_memes(telegram_id):
    user = Users.objects.filter(telegram_id=telegram_id).first()
    return Memes.objects.filter(user=user).all()


@sync_to_async()
def delete_user_meme(photo_id):
    Memes.objects.filter(photo_id=photo_id).delete()


@sync_to_async()
def get_all_memes():
    # user = Users.objects.filter(settings=True).first()
    return Memes.objects.all()


@sync_to_async()
def create_row_favorites(telegram_id, photo_id):
    user = Users.objects.filter(telegram_id=telegram_id).first()
    Favorites.objects.get_or_create(user=user, photo_id=photo_id)


@sync_to_async()
def get_user_favorites(telegram_id):
    user = Users.objects.filter(telegram_id=telegram_id).first()
    return Favorites.objects.filter(user=user).all()


@sync_to_async()
def delete_user_favorite(photo_id):
    Favorites.objects.filter(photo_id=photo_id).delete()
