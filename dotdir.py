from os import listdir
from os.path import isfile

from dotfile import Dotfile


class Dotdir:

    """Docstring for Dotdir."""

    def __init__(self, syspath, repopath):
        """TODO: to be defined."""
        self.dotfiles = []

        for path in listdir(syspath):
            if isfile(syspath + path):
                dotfile = Dotfile(path, syspath, repopath)
                self.dotfiles.append(dotfile)

    def copy_sync(self):
        """TODO: Docstring for copy_sync"""
        for dotfile in self.dotfiles:
            dotfile.copy_sync()
