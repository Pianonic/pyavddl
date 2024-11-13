# Pyamddl

**Pyamddl** stands for **Python Audio Metadata Direct Download Link**. It is a lightweight wrapper around `yt-dlp` that simplifies retrieving metadata and direct download links (DDL) for music from various platforms, including Spotify. This package allows you to easily access metadata and direct download links without the need to download the content.

## Features

- Retrieve direct download links (DDL) for music.
- Extract streaming information for individual songs.
- Support for playlists, albums, and individual songs.
- Optional integration with Spotify for enhanced search and metadata retrieval.

## Installation

To install the package, use pip:

```bash
pip install pyamddl
```

## Usage

### Setup

First, initialize the `PyamddlClient` by providing your Spotify credentials (optional):

```python
from pyamddl import setup

client = setup(spotify_client_id='your_spotify_client_id', spotify_client_secret='your_spotify_client_secret')
```

### Retrieve Music URLs

To retrieve URLs for playlists, albums, or individual songs based on a query:

```python
import asyncio

async def get_urls():
    urls = await client.get_music_urls('your_search_query')
    print(urls)

asyncio.run(get_urls())
```

### Retrieve Streaming Information for a Single Song

To get streaming information for an individual song:

```python
async def get_song_info():
    song_info = await client.get_song_streaming_url('song_url')
    print(song_info)

asyncio.run(get_song_info())
```

## License

This project is licensed under the CC-NC License. See the [LICENSE](LICENSE.md) file for details.
