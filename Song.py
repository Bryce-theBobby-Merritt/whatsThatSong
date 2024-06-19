class Song():
    def __init__(self, name: str, artist: str, uri: str, album_cover_path: str) -> None:
        self._name = name
        self._artist = artist
        self._uri = uri
        self._album_cover_path = album_cover_path


    def get_name(self) -> str:
        return self._name
    

    def get_artist(self) -> str:
        return self._artist
    

    def get_song_uri(self) -> str:
        return self._uri
    

    def get_album_cover_url(self) -> str:
        return self._album_cover_path


    def __eq__(self, other) -> bool:
        return (self._name is other.get_name() and self._artist is other.get_artist())
    