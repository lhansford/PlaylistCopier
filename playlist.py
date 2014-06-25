from os.path import join

class Playlist():

	def __init__(self, playlist_path, prefix=None):
		self.playlist = self.read_playlist(playlist_path)
		if prefix:
			self.playlist = [join(prefix, x) for x in self.playlist]

	def read_playlist(self, path):
		""" Opens an M3U file and returns a list of paths to songs in playlist.
		"""
		with open(path, 'r') as f:
			return [line.strip() for line in f]

	def get_playlist(self):
		""" Returns the playlist (i.e. a list of song paths). """
		return self.playlist

	def __repr__(self):
		output = ""
		for i, song in enumerate(self.get_playlist(), start=1):
			output += (str(i) + ": " + song + "\n")
		return output