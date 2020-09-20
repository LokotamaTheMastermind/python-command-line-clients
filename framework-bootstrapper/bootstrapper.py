#--* coding utf-8 *--#
"""
I folded some long pieces of code for easier navigation!
"""

""" Needed modules """


""" This section defines the welcome banner `Framework Jumpstarter` """
from clint.textui import colored, puts, indent
from PyInquirer import prompt, Separator
from pyfiglet import Figlet
import os
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
        'type': 'input',
        'name': 'framework',
        'message': '* Enter the framework to jumpstart |',
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

""" Function for normal quickstarting of django projects """

""" Django jumpstart function """


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


""" Dotnet tool jumpstart function """


def dot_net_jumpstart():

    def using_web_development_application_type(answers):
        return answers['using_web_development_application_type']

    def not_using_web_development_application_type(answers):
        return not answers['using_web_development_application_type']

    extra_questions = [
        {
            'type': 'list',
            'name': 'application_type',
            'message': f'Enter the application type you want to bootstrap for {framework} |',
            'choices': [
                Separator("\n= Application Stuff ="),
                'Console Application',
                'Class Library',
                'WPF Application',
                'WPF Class Library',
                'WPF Custom Control Library',
                'WPF User Control Library',
                'Windows Forms (WinForms) Application',
                'Windows Forms (WinForms) Class library',
                Separator("\n= Service Workers ="),
                'Worker Service',
                Separator("\n= Web Service Workers ="),
                'ASP.NET Core gRPC Service',
                Separator("\n= Testing Stuff ="),
                'Unit Test Project',
                'NUnit 3 Test Project',
                'NUnit 3 Test Item',
                'xUnit Test Project',
                Separator("\n= Web Development Stuff ="),
                'ASP.NET Core Web App',
                'ASP.NET Core with React.js and Redux',
                'ASP.NET Core with React.js',
                'ASP.NET Core with Angular',
                'Blazor Server App',
                'ASP.NET Core Web App (Model-View-Controller)',
                'ASP.NET Core Empty',
                'Blazor WebAssembly App',
                Separator("\n= Web Development Utilities ="),
                'Razor Class Library',
                'MVC ViewImports',
                'MVC ViewStart',
                Separator("\n= Web Development Extras ="),
                'Razor Component',
                'Razor Page',
                Separator("\n= APIS ="),
                'ASP.NET Core Web API',
                Separator("\n= Global Stuff ="),
                '.gitignore file',
                'global.json file',
                'NuGet Config',
                'Dotnet local tool manifest file',
                'Web Config',
                'Solution File',
                'Protocol Buffer File',
            ],
        },
        {
            'type': 'list',
            'name': 'programming_language',
            'message': 'Programming Language to use |',
            'choices': [
                'C#',
                'F#',
                'Visual Basic',
            ],
        },
        {
            'type': 'confirm',
            'name': 'using_web_development_application_type',
            'message': 'Please are you using a infrastructure under `Web Development Stuff` |',
            'default': False,
        },
        {
            'type': 'checkbox',
            'name': 'web_development_settings',
            'message': 'You\'re using a `Web Development application` type. Would you like the following options alongside the jumpstart',
            'when': using_web_development_application_type,
            'choices': [
                {
                    'name': 'Use authentication'
                },
                {
                    'name': 'Use browser link'
                },
                {
                    'name': 'Skip restoration'
                },
                {
                    'name': 'Remove https:// schema'
                }
            ]
        },
        {
            'type': 'checkbox',
            'name': 'base_settings',
            'message': 'This is the base settings for most dotnet generated projects, please select one\'s neccessary',
            'choices': [
                {
                    'name': 'Skip restoration',
                }
            ],
            'when': not_using_web_development_application_type,
        }
    ]

    answers = prompt(extra_questions)
    infrastructure = answers['application_type']
    programming_language = answers['programming_language']
    is_web_development_application = answers['using_web_development_application_type']

    if is_web_development_application:
        web_development_settings = answers['web_development_settings']
    else:
        web_development_settings = None

    if is_web_development_application:
        base_settings = None
    elif not is_web_development_application:
        base_settings = answers['base_settings']

    if infrastructure != None and programming_language != "":
        puts()
        puts(f'{colored.green("Setting up project")}: Archetecture - {infrastructure} | Programming Language - {programming_language}')
        puts()
        puts(f'{colored.cyan("Using tool of ")}{colored.green("dotnet")} for bootstrapping the project')

        import os
        import platform

        is_sub_directory = is_in_a_sub_folder

        infrastructure_short_names = {
            "Console Application": "console",
            "Class library": "classlib",
            "WPF Application": "wpf",
            "WPF Class library": "wpflib",
            "WPF Custom Control Library": "wpfcustomcontrollib",
            "WPF User Control Library": "wpfusercontrollib",
            "Windows Forms (WinForms) Application": "winforms",
            "Windows Forms (WinForms) Class library": "winformslib",
            "Worker Service": "worker",
            "Unit Test Project": "mstest",
            "NUnit 3 Test Project": "nunit",
            "NUnit 3 Test Item": "nunit-test",
            "xUnit Test Project": "xunit",
            "Razor Component": "razorcomponent",
            "Razor Page": "page",
            "MVC ViewImports": "viewimports",
            "MVC ViewStart": "viewstart",
            "Blazor Server App": "blazorserver",
            "Blazor WebAssembly App": "blazorwasm",
            "ASP.NET Core Empty": "web",
            "ASP.NET Core Web App (Model-View-Controller)": "mvc",
            "ASP.NET Core with React.js and Redux": "reactredux",
            "ASP.NET Core with React.js": "react",
            "ASP.NET Core with Angular": "angular",
            "ASP.NET Core Web App": "webapp",
            "Razor Class Library": "razorclasslib",
            "ASP.NET Core Web API": "webapi",
            "ASP.NET Core gRPC Service": "grpc",
            "Dotnet local tool manifest file": "tool-manifest",
            "global.json file": "globaljson",
            ".gitignore file": "gitignore",
            "Protocol Buffer File": "proto",
            "Solution File": "sln",
            "Web Config": "webconfig",
            "NuGet Config": "nugetconfig",
        }

        if is_sub_directory:

            op = platform.system()

            selected = infrastructure_short_names.get(infrastructure)

            if op == "Windows":
                os.system('cd "{}" && mkdir src && cd src && dotnet new {}'.format(
                    project_location, selected))
            elif op == "Darwin" or op == "Linux":
                os.system('cd "{}" && mkdir src && cd src && dotnet new {}'.format(
                    project_location, selected))

        elif not is_sub_directory:

            op = platform.system()

            selected = infrastructure_short_names.get(infrastructure)

            if op == "Windows":
                os.system('cd "{}" {}'.format(project_location, os.system(
                    'dotnet new {}'.format(selected))))
            elif op == "Darwin" or op == "Linux":
                os.system('cd "{}" && {}'.format(project_location, os.system(
                    'dotnet new {}'.format(selected))))


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
        elif framework == ".net":
            dot_net_jumpstart()

    elif location_of_preset == None:
        puts(
            f"{colored.magenta('Warning')}: Sorry can't find framework preset specified!\n")
    else:
        puts(f"{colored.red('Fatal error')}: Irreversible mistake has occured\n")

elif framework == "":
    puts(f'\n{colored.red("Error")}: Can\'t have an empty framework {colored.yellow("preset")} field!\n')
    exit()
