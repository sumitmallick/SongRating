# service/song_service.py
from repository.song_repo import SongRepository

class SongService:
    def __init__(self, song_repo):
        self.song_repo = song_repo

    def get_paginated_songs(self, page, per_page):
        return self.song_repo.get_songs_for_page(page, per_page)
        

    def get_song_by_title(self, title):
        return self.song_repo.get_song_by_title(title)

    def rate_song(self, song_id, rating):
        return self.song_repo.rate_song(song_id, rating)

