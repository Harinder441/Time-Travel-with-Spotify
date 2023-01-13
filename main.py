from spotify_class import MySpotify
from getsongslist import generate_top25
from art import logo

print(logo)
# get the popular songs of given date
date = input("Which date you want to go.(yyyy-mm-dd) ")
songs = generate_top25(date=date)
spotipy = MySpotify()
songs_uri = [spotipy.get_spotify_uri(song) for song in songs]
# remove empty strings
songs_uri = [uri for uri in songs_uri if uri]
playlist_id = spotipy.create_playlist(name=f"BillBoard top 25 of {date}")
spotipy.add_to_playlist(playlist_id, songs_uri)
