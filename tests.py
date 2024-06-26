import unittest
from Song import Song
from Game import Game

class SongMethodsTestCase(unittest.TestCase):
    def setUp(self):
        self.s1 = Song("S1", "A1", "S1.wav", "S1.png")

    
    def testSongEqMethod(self):
        sameArtistDifferentSong = Song("S2", "A1", "S2.wav", "S2.png")
        sameSongDifferentArtist = Song("S1", "A2", "S1.wav", "S1.png")
        sameSong                = Song("S1", "A1", "S1.wav", "S1.png")
        self.assertFalse(self.s1.__eq__(sameArtistDifferentSong))
        self.assertFalse(self.s1.__eq__(sameSongDifferentArtist))
        self.assertTrue(self.s1.__eq__(sameSong))


class GameMethodsTestCase(unittest.TestCase):
    def setUp(self):
        self.g = Game()
        Game.set_playlist_link("www.spotify.com/1234")


if __name__ == '__main__':
    unittest.main(verbosity=2)