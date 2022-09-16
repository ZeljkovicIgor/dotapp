import os
from os.path import exists
from shutil import copy
import sys

from textcolors import print_success


class Dotfile:

    """Class that represents a dotfile with its name and system and repo paths"""

    TEMP = "./test/repo/tmp/"

    def __init__(self, name, syspath, repopath):
        """Dotfile constructor

        :name: name of a file
        :syspath: system path of a file
        :repopath: git repository path of a file

        """
        self.name = name
        self.syspath = syspath
        self.repopath = repopath

    def copy_install(self):
        """docstring for copy_install"""

        if exists(self.get_sys_filename()):
            print(
                f"{self.get_sys_filename()} already exists in system path. Skipping..."
            )

            return

        if not exists(self.get_repo_filename()):
            print(
                f"{self.get_repo_filename()} does not exist in repo. Cannot be installed."
            )

            return

        self.prepare_for_install()
        self.copy_dotfile(Dotfile.TEMP, self.syspath)
        os.remove(self.get_temp_filename())

    def copy_sync(self):
        """docstring for copy_sync"""
        if not exists(self.get_sys_filename()):
            print(f"{self.get_sys_filename()} does not exist in system.")

            return

        if not exists(self.get_repo_filename()):
            if not exists(self.repopath):
                print(
                    f"Repo directory {self.repopath} not found. Creating directory..."
                )
                os.makedirs(self.repopath)

            print(f"Copying {self.name}...")
            self.copy_dotfile(self.syspath, self.repopath)
        else:
            if self.equal():
                print(
                    f"{self.name} files are same in repo and system. No need to copy them."
                )

                return

            print(f"Copying {self.name}...")
            self.copy_dotfile(self.syspath, self.repopath)
            self.replace_username()

    def prepare_for_install(self):
        """docstring for prepare_for_install"""
        try:
            print("Preparing file for install...")
            with open(self.get_repo_filename(), "r") as repofile:
                lines = repofile.readlines()
            with open(self.get_temp_filename(), "x") as tempfile:
                for line in lines:
                    tempfile.write(
                        line.replace("DOTS-USERNAME", os.getlogin())
                        if self.ignore_username(line) and "DOTS-USERNAME" in line
                        else line
                    )
        except Exception as e:
            print("There was an error during file preparetion.")
            raise e

    def replace_username(self):
        """docstring for replace_username"""
        try:
            print("Replacing username...")
            with open(self.get_repo_filename(), "r") as file:
                lines = file.readlines()
            with open(self.get_repo_filename(), "w") as file:
                for line in lines:
                    file.write(
                        line.replace(os.getlogin(), "DOTS-USERNAME")
                        if self.ignore_username(line) and os.getlogin() in line
                        else line
                    )
        except Exception as e:
            print("There was an error during replacing username in file")
            raise e

    def copy_dotfile(self, src, dest):
        """docstring for copy_dotfile"""
        try:
            copy(src + self.name, dest)
        except Exception as e:
            print("There was an error while copying files: ")
            raise e
        else:
            print_success(f"{self.name} copied from {src} to {dest}")

    def ignore_username(self, line):
        """docstring for ignore_username"""
        return "##dots-ignore-username##" in line

    def equal(self):
        """docstring for equal"""

        def user_in_line(line):
            """docstring for user_in_line"""
            if self.ignore_username(line) and (
                "USERNAME" in line or os.getlogin() in line
            ):
                return False
            return True

        try:
            print("Comparing files in system and repo...")

            with open(self.get_sys_filename(), "r") as filesys, open(
                self.get_repo_filename(), "r"
            ) as filerepo:
                filesys_fil = list(filter(user_in_line, filesys))
                filerepo_fil = list(filter(user_in_line, filerepo))

                if len(filerepo_fil) != len(filesys_fil):
                    print(
                        f"{self.name} has {len(filesys_fil)} lines in system file and {len(filerepo_fil)} in repo file."
                    )
                    return False

                for index, linesys in enumerate(filesys_fil):
                    if linesys != filerepo_fil[index]:
                        return False

                return True
        except Exception as e:
            raise e

    def get_sys_filename(self):
        """get path to file in system"""
        return self.syspath + self.name

    def get_repo_filename(self):
        """get path to file in repo"""
        return self.repopath + self.name

    def get_temp_filename(self):
        """docstring for get_temp_filename"""
        return Dotfile.TEMP + self.name
