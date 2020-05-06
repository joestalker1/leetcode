from collections import defaultdict


class Solution:
    def userFavoriteGeneres(self, user_songs, genre_songs):
        if not genre_songs:
            return []
        res = defaultdict(list)
        song_to_genre = {song: genre for genre, list_of_songs in genre_songs.items() for song in list_of_songs}
        for user in user_songs.keys():
            genre_to_num = defaultdict(int)
            songs = user_songs[user]
            max_songs = 0
            for song in songs:
                genre_to_num[song_to_genre[song]] += 1
                max_songs = max(max_songs, genre_to_num[song_to_genre[song]])
            res[user] = [genre for genre, count in genre_to_num.items() if count == max_songs]
        return res


sol = Solution()
print(sol.userFavoriteGeneres({
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma": ["song5", "song6", "song7"]
},
    {
        "Rock": ["song1", "song3"],
        "Dubstep": ["song7"],
        "Techno": ["song2", "song4"],
        "Pop": ["song5", "song6"],
        "Jazz": ["song8", "song9"]
    }))
