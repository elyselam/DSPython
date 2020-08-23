class Song:
    def __init__ (self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)

class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("~/Downloads/albums.txt ", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)


if __name__ == '__main__':
    load_data()

