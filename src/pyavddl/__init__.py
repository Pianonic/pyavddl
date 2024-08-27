from typing import List
from .config import set_spotify_credentials
from .models.music_information import MusicInformation
from .platform_handlers import music_url_getter

class PyamddlClient:
    def __init__(self, spotify_client_id: str, spotify_client_secret: str):
        set_spotify_credentials(spotify_client_id, spotify_client_secret)
        
    async def get_music_urls(self, query: str) -> List[str]:
        """
        Retrieves URLs for playlists, albums, or individual songs based on the query.
        """
        return await music_url_getter.get_urls(query)
    
    async def get_song_streaming_url(self, song_url: str) -> MusicInformation:
        """
        Retrieves streaming information for a single song. Note: Only works with individual songs, not playlists or albums.
        """
        return await music_url_getter.get_streaming_url(song_url)
    
def setup(spotify_client_id: str = None, spotify_client_secret: str = None) -> PyamddlClient:
    """
    Initializes the PyavddlClient. Provide your own Spotify Credentials (Optional, will also work without).
    """
    return PyamddlClient(spotify_client_id, spotify_client_secret)
