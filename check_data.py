import json

# Load the JSON data from the file
with open('songs.json', 'r') as file:
    songs = json.load(file)

# Check if the expected keys are present
if all(key in songs for key in ['id', 'title']):
    # Extract the song IDs
    ids = [songs['id'][str(i)] for i in range(len(songs['id']))]  # Use string keys to access the IDs
    print("Song IDs:", ids)  # Print the list of IDs for verification

    # Extract song titles (optional)
    titles = [songs['title'][str(i)] for i in range(len(songs['title']))]  # Use string keys to access the titles
    print("Song Titles:", titles)  # Print the list of titles for verification

else:
    print("Error: Expected keys not found in the data.")
