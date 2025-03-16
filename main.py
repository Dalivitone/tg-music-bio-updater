import time
from telethon import TelegramClient, functions, errors
import config
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

cache_path = os.path.join(os.getcwd(), "token.cache")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=config.spotify_client_id,
    client_secret=config.spotify_client_secret,
    redirect_uri=config.spotify_redirect_uri,
    cache_path=cache_path,
    scope="user-read-currently-playing"
))

client = TelegramClient('spotify', config.api_id, config.api_hash)
client.start()

me = client.loop.run_until_complete(client.get_me())
status = ""
lastStatus = status

def updateStatus():
    global lastStatus
    while True:
        try:
            currentTrack = sp.currently_playing()
        except Exception as e:
            print("Error fetching song", e)
            return
        if currentTrack and currentTrack.get('is_playing'):
            name = currentTrack['item']['name']
            artist = currentTrack['item']['artists'][0]['name']
            newStatus = f"🎶Listening: {artist} - {name}"
        else:
            newStatus = status

        if len(newStatus) > 70:
            newStatus = newStatus[:70]
        
        if newStatus == lastStatus:
            time.sleep(20)
            continue
        
        try:
            client.loop.run_until_complete(client(functions.account.UpdateProfileRequest(about=newStatus)))
            lastStatus = newStatus
        except errors.FloodWaitError as e:
            print(f"Sleeping for {e.seconds} seconds")
            time.sleep(e.seconds + 1)
        except errors.AboutTooLongError as e:
            print("Too long bio")
        time.sleep(20)

try:
    while True:
        updateStatus()
        time.sleep(20)
except KeyboardInterrupt:
    try:
        client.loop.run_until_complete(client(functions.account.UpdateProfileRequest(about=status)))
    except Exception as e:
        print("Error resetting status", e)