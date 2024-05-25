# Lesson 3: Python Sets
# 3. Music Festival Playlist Organization

artist_names = ["Kendrick Lamar", "Drake", "J. Cole", "Kendrick Lamar", "Nas", "Jay-Z"]
unique_artists = set()

for artist in artist_names:
    unique_artists.add(artist)

duplicate_playlists_found = len(artist_names) != len(unique_artists)

print(f"Duplicate playlists found: {duplicate_playlists_found}")
