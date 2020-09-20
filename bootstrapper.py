""" Needed modules """
from clint.textui import colored, puts, indent
from PyInquirer import prompt, Separator
from pyfiglet import Figlet
import os


""" This section defines the welcome banner `Framework Jumpstarter` """
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


""" Set of neccessary questions """
questions = [
    {
        # Framework Jumpstarter
        'type': 'input',
        'name': 'framework',
        'message': '* Enter the framework to jumpstart and provide the boiler-template |',
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


""" Add optional frameworks here! """
framework_presets = [
    'asp.net',
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
project_name = answers['project_name']  # Project name grabbed for validation
# Project location for location of project
project_location = answers['location']


def django_jumpstart():
    """ Validate and initialize jumpstarting for each iterable in `framework_presets` """

    """ Step 1 - Validation: try to see if virtualenv package exists then update and if not install package! """
    try:
        """ Needed testing & important modules  """
        import virtualenv
        import os
        import platform
        op = platform.system()  # User-base operating system

        """ Update existing virtualenv package """
        """ Follows normal standard for updating packages for `pip` in windows and `pip3` in Mac or linux """
        if op == "Windows":
            os.system('pip install --upgrade virtualenv')
        elif op == "Darwin" or op == "Linux":
            os.system('pip3 install --upgrade virtualenv')
        else:
            """ Cases when python doesn't understand the user-operating system """
            with indent(4):
                puts(
                    f"{colored.red('Update Error')}: Couldn't jumpstart {framework} because of unknown system type")
                with indent(4):
                    puts('and operating system client is not recognized')
            exit()

    except ImportError:
        """ If virtualenv package not found then run this piece """
        """ Needed modules """
        import os
        import platform
        op = platform.system()  # User-based operating system

        """
        Install virtualenv package according to the various ways of installing packages using pip for different operating systems
        """
        if op == "Windows":
            os.system('pip install virtualenv')
        elif op == "Darwin" or op == "Linux":
            os.system('pip3 install virtualenv')
        else:
            with indent(4):
                puts(
                    f"{colored.red('Installation Error')}: Couldn't install and jumpstart {framework} because of missing package dependency")
                with indent(4):
                    puts('and operating system client is not recognized')
            exit()

    """ Step 2 - Django Bootstrapper: run the `django-admin` startproject command after creating virtualenv """
    import os

    root_dir = os.getcwd()
    virtualenv = os.path.exists(f"{root_dir}/venv")

    if virtualenv:
        import platform
        op = platform.system()  # User-based operating system

        if op == "Windows":
            activation = os.system(
                '{}/venv/Scripts/activate'.format(root_dir))
            if activation == 0:
                os.system(
                    '{}/venv/Scripts/activate && pip install django'.format(root_dir))
                """
                This runs an Windows command for changing directory to the `project_location` and then starting activates a virtualenv and then it starts a project based on value specified in `project_name`
                """
                os.system('cd "{}" && {}/venv/Scripts/activate && django-admin startproject {} .'.format(
                    project_location, root_dir, project_name))
            elif activation == 1:
                puts(
                    f'{colored.red("Activation Error")}: this occured when activating virtualenv!')


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
            django_jumpstart()

    elif location_of_preset == None:
        puts(f"\n{colored.orange('Warning')}: Sorry can't find framework preset specified!\n")
    else:
        puts(f"\n{colored.red('Fatal error')}: Irreversible mistake has occured\n")

elif framework == "":
    puts(f'\n{colored.red("Error")}: Can\'t have an empty framework {colored.yellow("preset")} field!\n')
    exit()
