from app.models.Database import Users as Users_, Musics


def Users():
    return [i for i in Users_.select()]


def Statistica():
    all_musics = Musics.select().count()
    users = Users_.select().count()
    return [users, all_musics]


def User(chat_id):
    try:
        Users_.create(chat_id=chat_id)
    except:
        pass
