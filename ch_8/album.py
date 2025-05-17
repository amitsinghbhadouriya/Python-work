def make_album(artist, title, num_songs=None):
    album = {
        'artist': artist,
        'title': title
    }
    if num_songs is not None:
        album['num_songs'] = num_songs
    return album

album1 = make_album("Taylor Swift", "Fearless")
album2 = make_album("Ed Sheeran", "Divide", num_songs=16)
album3 = make_album("Adele", "21", num_songs=11)

print(album1)
print(album2)
print(album3)
