from peewee import fn

from app.models.Database import Musics as Music


class Musics:
    def __init__(self, searched_text):
        self.searched_text = searched_text

    def Search_Music(self, limit=False, offset=0):
        if offset:
            return [i for i in
                    Music.select().where(fn.Lower(Music.title).contains(self.searched_text)).limit().offset(offset)]
        else:
            return [i for i in
                    Music.select().where(fn.Lower(Music.title).contains(self.searched_text)).paginate(limit, 10)]

    def Search_Inline_Music(self, offset=False, types=False):
        if types:
            return Music.select().where(fn.Lower(Music.title).contains(self.searched_text)).count()
        if type(offset) == int:
            return [i for i in
                    Music.select().where(fn.Lower(Music.title).contains(self.searched_text)).limit(50).offset(
                        offset - 1)]

    def All_Music(self):
        return Music.select().where(Music.title.contains(self.searched_text)).count()


def Get_Music(mp3_id):
    return Music.select(Music.file_id).where(Music.id == mp3_id)


def New_Music(title, file_id):
    try:
        if not Music.select().where(Music.title == title):
            Music.create(title=title, file_id=file_id)
            return "Musiqa bazaga joylandi."
        else:
            return "Musiqa avvaldan mavjud."
    except:
        return 'Musiqa bazaga joylanmadi.'


def Update_Count(music_id):
    Music.update(counts=Music.counts + 1).where(Music.id ==
                                                int(music_id)).execute()


def Get_count(page=False):
    if not page:
        return Music.select().where(Music.counts != 0).limit(1000).order_by(Music.counts.desc()).count()
    else:
        return [i for i in Music.select().where(Music.counts > 0).paginate(page, 10).order_by(Music.counts.desc())]
