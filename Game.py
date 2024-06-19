from Song import Song

class Game():
    def __init__(self):
        self._playlist_link = ""
        self._all_songs = []
        self._correctly_guessed = []
        self._incorrectly_guessed = []
        self._lives = 3
        self._current_song = None


    def set_playlist_link(self, playlist_link:str) -> None:
        self._playlist_link = playlist_link


    #should only be used for testing
    def get_playlist_link(self) -> str:
        return self._playlist_link
    

    def get_lives(self) -> int:
        return self._lives
    

    def get_current_song(self) -> Song:
        return self._current_song
    
