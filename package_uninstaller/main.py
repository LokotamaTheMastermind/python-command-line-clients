from clint.textui import puts, indent, colored
from pyfiglet import Figlet
from PyInquirer import prompt
from extra import welcome_banner
from extra.global_vars import questions
from package_managers import *


# Entry point in function
def entry():
    welcome_banner()  # Welcome banner display
    print("")
    answers = prompt(questions)  # Questions
    package_manager = answers['package_manager'].lower()  # Lower case answers
    # Is it a containerized project package
    is_local = answers['folder_packages']

    if is_local:
        is_local = answers['folder_packages']
        is_global = False
    elif not is_local:
        is_global = answers['global_packages']
        is_local = False
    # Calls action() function with param of `package_manager`
    main_action(package_manager, is_global, is_local)


def validate(folder_path):
    pass


def main_action(package_manager, global_package, containerized_package):

    import os
    import platform
    import click
    import re

    op = platform.system()  # Operating system

    if op == "Windows":

        if package_manager == "pip":
            windows_pip(global_package, containerized_package)

        elif package_manager == "yarn":
            windows_yarn(global_package, containerized_package)

        elif package_manager == "composer":

            # Continue here tomorrow --> after tomorrow
            if global_package and not containerized_package:
                pass
            elif not global_package and containerized_package:
                pass

        elif package_manager == "chocolatey":
            pass

        elif package_manager == "npm":
            pass

    elif op == "Darwin":

        if package_manager == "pip":
            pass

        elif package_manager == "yarn":
            pass

        elif package_manager == "composer":

            pass

            # Continue here tomorrow --> after tomorrow
            if global_package and not containerized_package:
                pass
            elif not global_package and containerized_package:
                pass

        elif package_manager == "npm":
            pass

        elif package_manager == "homebrew":
            pass


if __name__ == "__main__":
    entry()


"""
This file doesn't yet support using files in another drive like `D:` or `A:` apart from `C:` drive that
comes default to Windows
"""
