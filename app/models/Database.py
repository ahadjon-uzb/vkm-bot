from peewee import SqliteDatabase, Model, BigIntegerField, TextField

db = SqliteDatabase('vkm_bot.db')


class Users(Model):
    chat_id = BigIntegerField(primary_key=True)

    class Meta:
        database = db


class Musics(Model):
    title = TextField()
    file_id = TextField()
    counts = BigIntegerField(default=0)

    class Meta:
        database = db


class Playlist(Model):
    title = TextField()
    file_id = TextField()
    user_id = BigIntegerField()
    music_id = TextField()

    class Meta:
        database = db


db.connect()
db.create_tables([Users, Musics, Playlist])
