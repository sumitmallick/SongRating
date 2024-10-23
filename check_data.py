import json

with open('songs.json', 'r') as file:
    songs = json.load(file)

if all(key in songs for key in ['id', 'title']):
    ids = [songs['id'][str(i)] for i in range(len(songs['id']))]
    print("Song IDs:", ids)

    titles = [songs['title'][str(i)] for i in range(len(songs['title']))]
    print("Song Titles:", titles)

else:
    print("Error: Expected keys not found in the data.")
