from Song import Song
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import dotenv
import requests
import base64
import os


class Game():
    def __init__(self):
        self._playlist_id = ""
        self._all_songs = []
        self._correctly_guessed = []
        self._incorrectly_guessed = []
        self._lives = 3
        self._current_song = None
        self._API_URL_BASE = "https://api.spotify.com/v1"

        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        dotenv.load_dotenv(dotenv_path)


    def guess_song(self, guess: str) -> None:
        if (self._current_song.get_name().upper() is guess.upper()):
            #If correct guess: increase score, go next song
            pass
        else:
            #If incorrect guess: decrease lives.
            pass


    def set_playlist_id(self, playlist_id: str) -> None:
        self._playlist_id = playlist_id

    
    def get_all_tracks_from_playlist_id(self) -> None:
        self._all_songs.clear()

        config = dotenv.dotenv_values(".env")

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic " + base64.b64encode((os.environ.get("SPOTIPY_CLIENT_ID") + ":" + os.environ.get("SPOTIPY_CLIENT_SECRET")).encode("ascii")).decode("ascii")
        }

        payload = {
            "grant_type": "client_credentials"
        }

        results = requests.post("https://accounts.spotify.com/api/token", data=payload, headers=headers).json()
        if results:
            os.environ["SPOTIPY_ACCESS_TOKEN"] = results["access_token"]
            print(f"Generated Access Token for {results["expires_in"]} seconds with the type: {results["token_type"]}")

        #now that we have established an access token (that typically last 3600 seconds), we can start making fetch calls=

        headers = {
            "Authorization": "Bearer " + os.environ.get("SPOTIPY_ACCESS_TOKEN")
        }

        results = requests.get(self._API_URL_BASE + f"/playlists/{self._playlist_id}/tracks", headers=headers).json()
    
        #form of: (name, forst artist, album, uri) 

        compact_res = [(item["track"]["name"], item["track"]["artists"][0]["name"],item["track"]["album"]["name"],item["track"]["uri"]) for item in results["items"]]

        for item in compact_res:
            temp = Song(item[0], item[1], item[3], item[2])        
            self._all_songs.append(temp)



    def get_all_songs(self) -> list[Song]:
        return self._all_songs
    
    
    def get_all_song_names(self) -> list[str]:
        return [s.get_name() for s in self._all_songs]


    #should only be used for testing
    def get_playlist_link(self) -> str:
        return self._playlist_link
    

    def get_lives(self) -> int:
        return self._lives
    

    def get_current_song(self) -> Song:
        return self._current_song
    

    def ready_game(self) -> None:
        random.shuffle(self._all_songs)
        self._current_song = self._all_songs.pop(0)

        res = SpotifyOAuth(scope="user-read-playback-state, user-modify-playback-state").get_access_token()
        self.sp = spotipy.Spotify(auth=res["access_token"])


    def play_song_from_id(self, song_id_uri: str) -> None:
        headers = {
            "Authorization": "Bearer" + os.environ.get("SPOTIPY_ACCESS_TOKEN")
        }

        body = {
            "uri": f"{song_id_uri}"
        }

        results = requests.post(self._API_URL_BASE + "/me/player/play", data=body, headers=headers).json()
        if results["error"]:
            self.sp.start_playback(uris=[song_id_uri])

    
    def start(self) -> None:
        print("[STARTING GAME]")
        self.play_song_from_id(self._current_song.get_song_uri())
        pass
