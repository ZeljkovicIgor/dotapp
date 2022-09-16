import os
from os.path import exists
import sys
from utils import is_tool


class Dependency:

    """Docstring for Dependency."""

    def __init__(self, text, prerequisites, commands, alias="", path=""):
        """TODO: to be defined.

        :exists: TODO
        :prerequisites: TODO
        :commands: TODO

        """
        self.text = text
        self.prerequisites = prerequisites
        self.commands = commands
        self.alias = alias
        self.path = path

    def exists(self):
        """docstring for exists"""
        if self.path:
            return exists(self.path)
        else:
            return is_tool(self.alias)

    def install(self):
        """docstring for install"""
        if self.exists():
            return

        if not self.prerequisites_satisfied():
            return

        if not self.confirm_install():
            return

        for command in self.commands:
            try:
                print(f"Installing {self.text}...\n")
                # os.system(command)
            except Exception as e:
                raise e
            else:
                print(f"{self.text} successfully installed.\n")

    def confirm_install(self):
        """docstring for confirm_install"""
        choice = input(
            f"Dependency {self.text} is about to be installed. Are you sure you want to continue? (Y/n)"
        )

        if choice not in ["y", "Y", "n", "N", ""]:
            print("You must enter a valid input.")
            self.confirm_install()
        elif choice not in ["n", "N"]:
            return True
        else:
            return False

    def prerequisites_satisfied(self):
        """docstring for check_prerequisites"""
        for prereq in self.prerequisites:
            if isinstance(prereq, str):
                if not is_tool(prereq):
                    print(
                        f"Dependency {self.text} cannot be installed without {prereq}. Please install {prereq} first.\n"
                    )
                    return False
            else:
                if not exists(prereq["path"]):
                    print(
                        f"Dependency {self.text} cannot be installed without {prereq['path']}. Please install {prereq['path']} first.\n"
                    )
                    return False

        return True
