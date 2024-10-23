# load_data.py
import json
from models.song import Song, db

def load_data_to_db(json_file):
    if Song.query.count() == 0:
        with open(json_file, 'r') as f:
            data = json.load(f)

        songs = []
        for i in range(len(data['id'])):
            song = Song(
                id=data['id'][str(i)],
                title=data['title'][str(i)],
                danceability=data['danceability'][str(i)],
                energy=data['energy'][str(i)],
                key=data['key'][str(i)],
                loudness=data['loudness'][str(i)],
                mode=data['mode'][str(i)],
                acousticness=data['acousticness'][str(i)],
                instrumentalness=data['instrumentalness'][str(i)],
                liveness=data['liveness'][str(i)],
                valence=data['valence'][str(i)],
                tempo=data['tempo'][str(i)],
                duration_ms=data['duration_ms'][str(i)],
                time_signature=data['time_signature'][str(i)],
                num_bars=data['num_bars'][str(i)],
                num_sections=data['num_sections'][str(i)],
                num_segments=data['num_segments'][str(i)],
                class_type=data['class'][str(i)]
            )
            songs.append(song)

        db.session.bulk_save_objects(songs)
        db.session.commit()
        print(f"Loaded {len(songs)} songs into the database.")
    else:
        print("Database already contains data. Skipping load.")
