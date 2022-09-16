from typing import List
from dotfile import Dotfile
from utils import is_tool


class Dot:

    """Class that represents a dot"""

    def __init__(self, name, text, files: List[Dotfile], dependencies: List):
        """Dot constructor"""
        self.name = name
        self.text = text
        self.files = files
        self.dependencies = dependencies

    def sync(self):
        """Method for syncing dotfiles from system to repo"""

        if self.name and not is_tool(self.name):
            print(f"{self.text} is not installed.\n")
            return

        for file in self.files:
            file.copy_sync()

    def install(self):
        """Method for installing tools and initializing dots on the system

        :returns: void

        """
        for file in self.files:
            file.copy_install()

    def update(self):
        """Method for updating dotfiles from repo to system

        :returns: void

        """
        pass
