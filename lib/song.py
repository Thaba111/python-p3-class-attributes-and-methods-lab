#song class: can produce individual songs
#each song has : name, artist, genre
#song class should track the numbe rof songs created

class Song:
    count = 0
    genre_count = {}
    artist_count = {}
    genres = set()
    artists = set()

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres.add(genre)
        Song.artists.add(artist)
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1
        

    @classmethod
    def most_prolific_artist(cls):
        max_songs = max(cls.artist_count.values())
        prolific_artists = [artist for artist, count in cls.artist_count.items() if count == max_songs]
        print(f"The most prolific artist(s): {', '.join(prolific_artists)}")
        return prolific_artists

    @classmethod
    def most_common_genre(cls):
        max_count = max(cls.genre_count.values())
        common_genres = [genre for genre, count in cls.genre_count.items() if count == max_count]
        return common_genres

   


#test case
song1 = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("Halo", "Beyonce", "Pop")

print("Song 1:", song1.name, "by", song1.artist, "(", song1.genre, ")")
print("Song 2:", song2.name, "by", song2.artist, "(", song2.genre, ")")
# Check the count of songs
print("Total number of songs created:", Song.count)
# Check the genres and artists
print("Genres:", Song.genres)
print("Artists:", Song.artists)
# Check the genre count and artist count
print("Genre count:", Song.genre_count)
print("Artist count:", Song.artist_count)

# Find the most prolific artist and most common genre
most_prolific_artist = Song.most_prolific_artist()
most_common_genre = Song.most_common_genre()
    

