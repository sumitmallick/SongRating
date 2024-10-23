# repository/song_repo.py
from models.song import Song, db

class SongRepository:
    def __init__(self):
        pass

    def load_data(self, json_data):
        num_items = len(json_data['id'])
        for i in range(num_items):
            song = Song(
                id=json_data['id'][str(i)],
                title=json_data['title'][str(i)],
                danceability=json_data.get('danceability', {}).get(str(i), None),
                energy=json_data.get('energy', {}).get(str(i), None),
                mood=json_data.get('mood', {}).get(str(i), None),
                acousticness=json_data.get('acousticness', {}).get(str(i), None),
                tempo=json_data.get('tempo', {}).get(str(i), None),
                duration_ms=json_data.get('duration_ms', {}).get(str(i), None),
                num_sections=json_data.get('num_sections', {}).get(str(i), None),
                num_segments=json_data.get('num_segments', {}).get(str(i), None)
            )
            db.session.add(song)
        db.session.commit()

    def get_songs_for_page(self, page, per_page):
        pagination = Song.query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total

    def get_song_by_title(self, title):
        return Song.query.filter_by(title=title).first()

    def rate_song(self, song_id, rating):
        song = Song.query.get(song_id)
        if song:
            song.rating = rating
            db.session.commit()
            return song
        return None
