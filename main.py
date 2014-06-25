from os.path import isfile, isdir, basename
from shutil import copy

import click

from playlist import Playlist

def copy_file(path, destination):
	""" Copies the file at the given path to the given destination. Path must 
		be a file and destination must be a directory.
	"""
	if not isfile(path):
		raise IOError("File " + path + " does not exist.")
	if not isdir(destination):
		raise IOError("Directory " + destination + " does not exist.")
	click.echo("Copying " + basename(path))
	copy(path, destination)

def get_playlist(playlist_path, dir_prefix=None):
	""" Returns a playlist object built from the given path. A directory prefix
		can be supplied if the playlist's paths are not absolute (useful for 
		playlists made with MPD).
	"""
	return Playlist(playlist_path, dir_prefix)

def print_playlist(playlist_path, dir_prefix=None):
	"""	Prints the given playlist. """
	click.echo(Playlist(playlist_path, dir_prefix))

def copy_playlist_files(file_list, destination):
	""" Copy all files in the given list to the given destination. """
	for song in file_list:
		copy_file(song, destination)

@click.command()
@click.argument('playlist', type=click.Path(exists=True))
@click.argument('destination', type=click.Path(exists=True))
@click.option('-p', '--prefix', default=None, help="Optional prefix for playlist files. Useful if playlist created in MPD.")
@click.option('-c', '--confirm', is_flag=True, help="Print playlist and get confirmation before copying.")
def run(playlist, destination, prefix, confirm):
	if confirm:
		print_playlist(playlist, prefix)
		response = ""
		try:
			input = raw_input
		except NameError:
			pass
		while response not in ['y','n']:
			response = input("Copy playlist? (y/n)\n")
		if response == "n":
			return None
	playlist_obj = get_playlist(playlist, prefix)
	# Copy playlist file
	copy_file(playlist, destination)
	copy_playlist_files(playlist_obj.get_playlist(), destination)

if __name__ == '__main__':
    run()
