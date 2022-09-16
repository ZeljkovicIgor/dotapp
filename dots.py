#!/usr/bin/python
""" Script for working with dot files this being the main file where the menu is made """

import os
import sys
from dotsinventory import DotsInventory

main_menu_options = ["Install", "Update", "Sync", "Exit"]
tool_menu_options = []

dotinventory = DotsInventory()


def initialize():
    """initialize the app by mapping all data to objects and add them to menu options"""
    tool_menu_options.extend([dotinventory] + dotinventory.get_all() + ["Back"])


def print_menu(menu_options):
    """function to initialize main menu"""
    for index, tool in enumerate(menu_options):
        print(index, "--", tool if isinstance(tool, str) else tool.text)


def handle_action(action, tool):
    """docstring for handleAction"""
    if main_menu_options[action] == "Install":
        tool_menu_options[tool].install()

    if main_menu_options[action] == "Update":
        tool_menu_options[tool].update()

    if main_menu_options[action] == "Sync":
        tool_menu_options[tool].sync()


def show_submenu(action):
    """docstring for submenu"""

    while True:
        print_menu(tool_menu_options)
        try:
            tool = int(input("Enter your choice: "))
        except ValueError:
            print("Wrong input. Please enter a number\n")
        except KeyboardInterrupt:
            sys.exit()
        else:
            if tool == len(tool_menu_options) - 1:
                print("Going back...\n")
                break
            if tool > len(tool_menu_options) - 1 or tool < 0:
                os.system("clear")
                print(
                    f"Invalid option. Please enter a number between 0 and {len(tool_menu_options) - 1}.\n"
                )

            os.system("clear")
            handle_action(action, tool)


def show_menu():
    """docstring for menu"""

    while True:
        print_menu(main_menu_options)
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            os.system("clear")
            print("Wrong input. Please enter a number...\n")
        except KeyboardInterrupt:
            sys.exit()
        else:
            if option > len(main_menu_options) - 1 or option < 0:
                os.system("clear")
                print("Invalid option. Please enter a number between 1 and 4.\n")
            elif option == len(main_menu_options) - 1:
                print("Exiting...\n")
                sys.exit()
            else:
                os.system("clear")
                show_submenu(option)


initialize()
show_menu()
