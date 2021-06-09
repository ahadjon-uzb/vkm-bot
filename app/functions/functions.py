from app.models.Database import Playlist


class Playlists:
    def __init__(self, user_id, music_id=False):
        self.music_id = music_id
        self.user_id = user_id

    def lists(self, limit):
        return [i for i in Playlist.select().where(Playlist.user_id == self.user_id).paginate(limit, 10)]

    def lists_count(self):
        return Playlist.select().where(Playlist.user_id == self.user_id).count()

    def get_lists(self) -> list:
        music = Playlist.select().where(Playlist.user_id == self.user_id,
                                        Playlist.music_id == self.music_id)
        musics = []
        for m in music:
            musics.append(m.id)
        return musics

    def delete_or_add(self, file_id, title):
        if len(self.get_lists()) == 0:
            Playlist.create(music_id=self.music_id,
                            user_id=self.user_id, title=title, file_id=file_id)
            return False
        else:
            Playlist.delete().where(Playlist.user_id == self.user_id,
                                    Playlist.music_id == self.music_id).execute()
            return True


def split_list(lst):
    for i in range(0, len(lst), 5):
        yield lst[i:i + 5]
