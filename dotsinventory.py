from data import DATA
from dependency import Dependency
from dotdir import Dotdir
from dotfile import Dotfile


class DotsInventory:

    """Docstring for DotsInventory."""

    def __init__(self):
        """TODO: to be defined."""
        self.text = "All"
        self.inventory = []

        for dot in DATA:
            dot_class = dot["class"]

            files = []
            dependencies = []

            for file in dot["files"]:
                if file.get("name"):
                    files.append(Dotfile(file["name"], file["path"], file["repo_path"]))
                else:
                    files.append(Dotdir(file["path"], file["repo_path"]))

            for dependency in dot["dependencies"]:
                dependencies.append(
                    Dependency(
                        dependency["text"],
                        dependency["prerequisites"],
                        dependency["commands"],
                        dependency.get("alias") or dependency.get("path"),
                    )
                )

            self.inventory.append(
                dot_class(dot.get("name"), dot["text"], files, dependencies)
            )

    def sync(self):
        """docstring for sync"""
        for dot in self.inventory:
            dot.sync()

    def install(self):
        """docstring for install"""
        for dot in self.inventory:
            dot.install()

    def get_all(self):
        """TODO: Docstring for getAll."""
        return self.inventory
