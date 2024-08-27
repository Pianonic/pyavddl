from spotdl import Spotdl

_spotify_credentials = {}
_spotdl_instance = None

def set_spotify_credentials(spotify_api_key: str, spotify_secret_key: str):
    """Set the Spotify credentials and create a Spotdl instance."""
    global _spotify_credentials, _spotdl_instance
    _spotify_credentials = {
        'spotify_api_key': spotify_api_key,
        'spotify_secret_key': spotify_secret_key
    }
    
    # Create a Spotdl instance using the credentials
    _spotdl_instance = Spotdl(client_id=spotify_api_key, client_secret=spotify_secret_key)

def get_spotify_instance():
    """Get the Spotify instance and Spotdl instance."""
    global _spotdl_instance
    return _spotdl_instance

def get_spotify_credentials():
    """Get the Spotify credentials and Spotdl instance."""
    global _spotify_credentials
    return _spotify_credentials

# Example usage:
# set_spotify_credentials('your_spotify_api_key', 'your_spotify_secret_key')
# spotdl_instance = get_spotify_credentials()
