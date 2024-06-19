class Song():
    def __init__(self, name: str, artist: str, path: str, album_cover_path: str) -> None:
        self._name = name
        self._artist = artist
        self._path = path
        self._album_cover_path = album_cover_path


    def get_name(self) -> str:
        return self._name
    

    def get_artist(self) -> str:
        return self._artist
    

    def get_song_path(self) -> str:
        return self._path
    

    def get_album_cover_path(self) -> str:
        return self._album_cover_path


    def __eq__(self, other) -> bool:
        return (self._name is other.get_name() and self._artist is other.get_artist())
    

s1 = Song("Potato", "PotatoDev", "Song_Potato.wav", "AC_Potato.png")
s2 = Song("Potato", "PotatoDev", "Song_Potato2.wav", "AC_Potato2.png")

print(s1.__eq__(s2))