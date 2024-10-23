from flask import jsonify, request
from service.song_service import SongService

class SongAPI:
    def __init__(self, song_service: SongService):
        self.song_service = song_service

    def get_all_songs(self):
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        songs = self.song_service.get_all_songs(page, per_page)
        return jsonify([song.to_dict() for song in songs])

    def get_song(self, song_id):
        song = self.song_service.get_song(song_id)
        if song:
            return jsonify(song.to_dict())
        return jsonify({"error": "Song not found"}), 404

    def create_song(self):
        data = request.json
        song = self.song_service.create_song(data)
        return jsonify(song.to_dict()), 201

    def update_song(self, song_id):
        data = request.json
        song = self.song_service.update_song(song_id, data)
        if song:
            return jsonify(song.to_dict())
        return jsonify({"error": "Song not found"}), 404

    def delete_song(self, song_id):
        if self.song_service.delete_song(song_id):
            return "", 204
        return jsonify({"error": "Song not found"}), 404

    def rate_song(self, song_id):
        rating = request.json.get('rating')
        song = self.song_service.rate_song(song_id, rating)
        if song:
            return jsonify(song.to_dict())
        return jsonify({"error": "Song not found"}), 404
