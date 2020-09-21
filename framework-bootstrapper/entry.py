# -*- coding utf-8 -*-#
"""
I folded some long pieces of code for easier navigation!
"""

""" Needed modules """

""" This section defines the welcome banner `Framework Jumpstarter` """


""" Run this script from the root of your empty project folder """
from clint.textui import colored, puts, indent
from PyInquirer import prompt
from functions import django_jumpstart, dot_net_jumpstart
from utils import welcome_banner, questions, framework_presets
import os
path = os.getcwd()  # Gets currents directory `/home/Desktop/testfolder`


""" Check root folder for `.git` folder """
git_repo = os.path.exists(f"{path}/.git")  # Checks existence of git repository


""" Welcome banner """
welcome_banner()

""" Neccessary for console design to look good """
puts("")


answers = prompt(questions)

# Framework preset entered into the set of available questions
framework = answers['framework']
# Project name grabbed for validation
project_name = answers['project_name']
# Project location for location of project
project_location = answers['location']
# Project located in sub-folder
is_in_a_sub_folder = answers['is_sub_folder']


if framework != "" and project_name != "" and project_location != "":
    """ Smart way of finding `items` in a list """
    try:
        location_of_preset = framework_presets.index(framework)
    except ValueError:
        location_of_preset = None

    if location_of_preset != None:
        puts(
            f"\n{colored.blue(f'You are using preset of {framework} to start project')}\n")
        if framework == "django":
            # Initiate django template jumpstart
            oython_jumpstart(framework, project_location,
                             project_name, is_in_a_sub_folder)
        elif framework == ".net":
            # Initiate dotnet template jumpstart
            dot_net_jumpstart(framework, is_in_a_sub_folder,
                              project_location, project_name, git_repo)

    elif location_of_preset == None:
        puts(
            f"{colored.magenta('Warning')}: Sorry can't find framework preset specified!\n")
    else:
        puts(f"{colored.red('Fatal error')}: Irreversible mistake has occured\n")

elif framework == "":
    puts(f'\n{colored.red("Error")}: Can\'t have an empty framework {colored.yellow("preset")} field!\n')
    exit()
