import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENTID = '0f2c8b4ef67d42beb0409048a759fa4d'
CLIENTSECRET = '9cf5588938d244a3b47a254200db7a52'
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= CLIENTID,
                                                           client_secret=CLIENTSECRET))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])