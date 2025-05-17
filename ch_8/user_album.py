def make_album(artist, title, num_songs=None):
    album = {
        'artist': artist,
        'title': title
    }
    if num_songs is not None:
        album['num_songs'] = num_songs
    return album

while True:
    print("Enter album information (or 'q' to quit):")
    artist = input("Enter artist name: ")
    if artist == 'q':
        break
    
    title = input("Enter album title: ")
    if title == 'q':
        break
    
    num_songs_input = input("Enter number of songs (press Enter to skip): ")
    if num_songs_input == 'q':
        break
    elif num_songs_input:
        num_songs = int(num_songs_input)
        album_info = make_album(artist, title, num_songs)
    else:
        album_info = make_album(artist, title)
    
    print("Album information:")
    print(album_info)
