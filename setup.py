import pathlib
from setuptools import setup, find_packages

setup(
    name="pyamddl",
    version="0.2.0",
    description="A lightweight wrapper around 'yt-dlp' that simplifies retrieving metadata and direct download links (DDL) with a single function call.",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="PianoNic",
    project_urls={
        "Documentation": "https://docs.pianonic.com/pyamddl",
        "Source": "https://github.com/Pianonic/pyamddl"
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers" ,
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities",
    ],
    python_requires=">=3.10",
    install_requires=[
        "yt_dlp",
        "pytube",
        "beautifulsoup4",
        "spotdl",
        "spotipy",
        "ytmusicapi"
    ],
    packages=find_packages(),
    include_package_data=True,
)