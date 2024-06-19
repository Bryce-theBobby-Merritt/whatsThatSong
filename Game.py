from Song import Song
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import dotenv

class Game():
    def __init__(self):
        self._playlist_id = ""
        self._all_songs = []
        self._correctly_guessed = []
        self._incorrectly_guessed = []
        self._lives = 3
        self._current_song = None

    def _randomize_playlist(self):
        random.shuffle(self._all_songs)


    def guess_song(self, guess: str) -> bool:
        return (self._current_song.get_name().upper() is guess.upper())


    def set_playlist_id(self, playlist_id: str) -> None:
        self._playlist_id = playlist_id

    
    def get_all_tracks_from_playlist_id(self) -> None:
        config = dotenv.dotenv_values(".env")
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-library-read", client_id=config["CID"], client_secret=config["SECRET"], redirect_uri=config["REDIRECT_URI"]))
        results = sp.playlist_tracks(f'spotify:playlist:{self._playlist_id}')
    
        for item in results["items"]:
            print(item["track"]["name"])


    #should only be used for testing
    def get_playlist_link(self) -> str:
        return self._playlist_link
    

    def get_lives(self) -> int:
        return self._lives
    

    def get_current_song(self) -> Song:
        return self._current_song
    
if __name__ == '__main__':
    g = Game()
    g.set_playlist_id("312Cr7cPq6bXu4b40ZB2DU")
