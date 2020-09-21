# -*- coding utf-8 -*-#
"""
I folded some long pieces of code for easier navigation!
"""

""" Needed modules """

""" This section defines the welcome banner `Framework Jumpstarter` """

from clint.textui import colored, puts, indent
from PyInquirer import prompt, Separator
from pyfiglet import Figlet
import os
from functions import django_jumpstart, dot_net_jumpstart
figlet = Figlet(font='slant')
header = 'Framework Jumpstarter'
puts(colored.green(figlet.renderText(header)))


""" Run this script from the root of your empty project folder """
path = os.getcwd()  # Gets currents directory `/home/Desktop/testfolder`


""" Check root folder for `.git` folder """
git_repo = os.path.exists(f"{path}/.git")  # Checks existence of git repository


""" Information banner with indentation! """
with indent(6, quote=f' {colored.cyan("~!>")} '):
    # Information
    first_line = colored.blue(
        'This is a command line client for jump starting any programming language framework supported')

    # More Information
    second_line = colored.yellow("List of available commands are coming soon!")

    # Quick tip
    third_line = colored.cyan(
        "Quick tip: all fields marked * are important and leaving them will result in an error or wrongly jumpstarted projects!")

    information = """ {} \n {} \n {} """.format(
        first_line, second_line, third_line)
    puts(information)

""" Neccessary for console design to look good """
puts("")


""" Set of neccessary startup questions """
questions = [
    {
        # Framework Jumpstarter
        'type': 'list',
        'name': 'framework',
        'message': '* Choose the framework to jumpstart |',
        'choices': [
            {
                'name': '.net'
            },
            {
                'name': 'django'
            },
            {
                'name': 'flask'
            },
            {
                'name': 'javascript'
            },
            {
                'name': 'php'
            },
        ],
    },
    {
        # Project name
        'type': 'input',
        'name': 'project_name',
        'message': f'* Name of project (myproject) |',
        'default': 'myproject',
    },
    {
        # Project location
        'type': 'input',
        'name': 'location',
        'message': '* Location of created project |'
    },
    {
        # Project in sub-folder [Y/N]
        'type': 'confirm',
        'name': 'is_sub_folder',
        'message': 'Do you want your project in a sub-folder?',
        'default': False
    },
    {
        # Additional project feature
        'type': 'checkbox',
        'name': 'additional_stuff',
        'message': 'Select more stuff your want for your project',
        'choices': [
            Separator('= General Stuff ='),
            {
                'name': 'Item 1'
            },
            {
                'name': 'Item 2'
            },
            {
                'name': 'Item 3'
            },
        ]
    },
]


""" List of all application frameworks for jumpstarting """
""" Add optional frameworks here! """
framework_presets = [
    '.net',
    'django',
    'flask',
    'c# (console)',
    'c++ (console)',
    'symfony',
    'laravel',
    'reactjs',
    'vuejs',
    'angularjs',
    'backbonejs',
    'aureliajs'
]

answers = prompt(questions)

# Framework preset entered into the set of available questions
framework = answers['framework']
# Project name grabbed for validation
project_name = answers['project_name']
# Project location for location of project
project_location = answers['location']
# Project located in sub-folder
is_in_a_sub_folder = answers['is_sub_folder']

""" Dotnet tool jumpstart function """


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
            django_jumpstart(framework, project_location, project_name)
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
