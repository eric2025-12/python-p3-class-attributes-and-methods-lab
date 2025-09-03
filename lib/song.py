class Song:
    # class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # update counters
        Song.count += 1

        # update genres
        if genre not in Song.genres:
            Song.genres.append(genre)
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1

        # update artists
        if artist not in Song.artists:
            Song.artists.append(artist)
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1

    @classmethod
    def reset_all(cls):
        """Reset all class attributes (useful for tests)."""
        cls.count = 0
        cls.genres = []
        cls.artists = []
        cls.genre_count = {}
        cls.artist_count = {}
