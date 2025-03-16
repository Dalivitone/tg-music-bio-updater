# tg-music-bio-updater
Heresy please ignore, but it's supposed to automatically update your telegram profile bio with the song you're currently listening to on Spotify.

You need to install these libraries: telethon, spotipy
```
pip install telethon spotipy
```

Edit config.py with your information
```
# Change the values of the variables below to your own values
api_id = 123456 # Telegram api id
api_hash = '' # Telegram api hash

spotify_client_id = '' # Spotify client id
spotify_client_secret = '' # Spotify client secret
spotify_redirect_uri = '' # Spotify redirect uri
```
Get Telegram API credentials: https://my.telegram.org/  
Create Spotify credentials: https://developer.spotify.com/dashboard

# Running the script
```
python main.py
```

# Stopping the script
Press Ctrl+C in the terminal to stop the script. It will restore your telegram bio to an empty string.

# Worth to notice
Avoid updating too frequently to avoid issues.  
Telegram has a character limit for profile bios. The script cuts off the status if it exceeds 70 characters.
