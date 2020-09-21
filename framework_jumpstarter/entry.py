# -*- coding utf-8 -*-#
"""
I folded some long pieces of code for easier navigation!
"""


""" Run this script from the root of your empty project folder """
from clint.textui import colored, puts, indent
from PyInquirer import prompt
from functions import python_jumpstart, dot_net_jumpstart
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
        if framework == "python":
            # Initiate python template jumpstart
            python_jumpstart(project_location, project_name,
                             framework, is_in_a_sub_folder, git_repo)
        elif framework == ".net":
            # Initiate dotnet template jumpstart
            dot_net_jumpstart(framework, is_in_a_sub_folder,
                              project_location, project_name, git_repo)

    elif location_of_preset == None:
        puts()
        puts(
            f"{colored.yellow('Warning', bold=True)}: Sorry can't find framework preset specified!")
    else:
        puts(
            f"{colored.red('Fatal error', bold=True)}: Irreversible mistake has occured\n")


# This was done because I was bored and wanted something filled in
# Fill free to remove it, it isn't really important
elif framework == "" and project_location != "" and project_name != "":
    puts(f'\n{colored.red("Error", bold=True)}: Can\'t have an empty framework {colored.yellow("preset")} field!')
    exit()
elif framework != "" and project_location == "" and project_name != "":
    puts(f'\n{colored.red("Error", bold=True)}: Can\'t have an empty location for the project. May soon add default {colored.yellow("creation location")}')
    exit()
elif framework != "" and project_location != "" and project_name == "":
    puts(f'\n{colored.red("Error", bold=True)}: Can\'t have an empty project {colored.yellow("name")} field!')
    exit()
elif framework == "" and project_location == "" and project_name != "":
    puts(f'\n{colored.red("Error", bold=True)}: Can\'t have an empty framework {colored.yellow("preset")} field and empty project {colored.yellow("location")}!')
    exit()
elif framework != "" and project_location == "" and project_name == "":
    puts(f'\n{colored.red("Error", bold=True)}: Can\'t have an empty project {colored.yellow("location")} and an empty project {colored.yellow("name")} fields!')
    exit()
