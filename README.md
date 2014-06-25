#Playlist Copier

This script will copy all files in a M3U playlist file to the given destination.

##Installation

To use Playlist Copier, you will need to have Python 2 or 3 installed. You will
also need to instal the Python module [Click](click.pocoo.org).

##Usage

To use Playlist Copier, run any of the following commands from the Terminal/Console/Command Line.

Copy the playlist files to the destination directory:

    python main.py /my/playlists/playlist.m3u /destination/for/files

Copy the playlist files to the destination directory with confirmation before hand (the playlist will be printed out):

    python main.py -c /my/playlists/playlist.m3u /destination/for/files

Add a prefix to the playlist files and then copy them to the destination directory.

    python main.py --prefix=/prefix/for/files/ /my/playlists/playlist.m3u /destination/for/files