import spotipy
from spotipy.oauth2 import SpotifyOAuth


class MySpotify:
    def __init__(self):
        #you have to get tyour own token.txt file
        self.spotify = spotipy.Spotify(
            auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                      cache_path="token.txt",
                                      client_id= YOUR_CLIENT_ID,
                                      client_secret= YOUR_CLIENT_SECRET,
                                      redirect_uri="http://example.com"))

    def get_spotify_uri(self, song_name):
        """return empty string if song not found"""
        song = self.spotify.search(song_name, limit=10, offset=0, type='track')
        try:
            song_uri = song['tracks']['items'][0]['uri']
            return song_uri
        except KeyError:
            return ""

    def create_playlist(self,name=f"Billboard Indian 25"):
        user_id = self.spotify.current_user()['id']
        playlist = self.spotify.user_playlist_create(user=user_id, name=name, public=False)
        playlist_id = playlist['id']
        return playlist_id

    def add_to_playlist(self,playlist_id,song_uris):
        self.spotify.playlist_add_items(playlist_id=playlist_id, items=song_uris)



