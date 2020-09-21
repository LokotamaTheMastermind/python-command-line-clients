# -*- coding: utf-8 -*-

from clint.textui import colored, puts
from PyInquirer import prompt, Separator

""" Dotnet tool jumpstart """


def dot_net_jumpstart(framework, is_in_a_sub_folder, project_location, project_name, is_git_repository):

    def using_web_development_application_type(answers):
        return answers['using_web_development_application_type']

    def not_using_web_development_application_type(answers):
        return not answers['using_web_development_application_type']

    """ More `framework` specific questions """
    extra_questions = [
        {
            'type': 'list',
            'name': 'application_type',
            'message': f'Enter the application type you want to bootstrap for .net |',
            'choices': [
                Separator("\n= Application Stuff ="),
                'Console Application',
                'Class library',
                'WPF Application',
                'WPF Class library',
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

    # Infrastructure short names for project creation
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

    if infrastructure != "" and programming_language != "":
        """ Status info on the bootstrapping """
        puts()
        puts(f'{colored.green("Setting up project")}: Archetecture - {infrastructure} | Programming Language - {programming_language}')
        puts()
        puts(f'{colored.cyan("Using tool of ")}{colored.green("dotnet")} {colored.cyan("for bootstrapping the project")}')
        puts()

        import os
        import platform

        is_sub_directory = is_in_a_sub_folder

        """ Decides what to do if the bootstrapper wants anything at all """

        # Base template for .dotnet generated projects
        gitignore_template = """
        bin/
        """

        if is_sub_directory:

            op = platform.system()  # Operating system
            # User selected infrastructure type searching the available short names for dotnet infrastructures
            selected = infrastructure_short_names.get(infrastructure)

            if op == "Windows":

                """
                Changes the directory into the `project_location` specified by the use and then makes a new directory using 
                `project_name` and goes into the directory and creates new project based on `selected` infrastructure, makes folder 
                git repository and then makes empty .gitignore file and prints text in the console and opens generated folder in 
                Windows Explorer->(Only for Windows) then opens google chrome and runs dotnet server->(Windows only too)
                """

                default_chrome_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

                os.system('cd "{}" && mkdir {} && cd {} && dotnet new {} && dotnet build && git init && type nul > .gitignore && echo Done bootstrapping project && echo Edit the template .gitignore file in the folder I created! && explorer . && echo Running ASP.NET server && {} && echo Opened Google Chrome application now visit the site on https://localhost:5000, this is where I will stop && dotnet run'.format(
                    project_location, project_name, project_name, selected, default_chrome_location))  # Commands all in one

                """ Opens created .gitignore and appends `gitignore_template` var contents to the file and then saves the file """
                with open('{}/{}/.gitignore'.format(project_location, project_name), "a") as gitignore_file:
                    gitignore_file.writelines(gitignore_template)

            elif op == "Darwin" or op == "Linux":

                """
                Changes the directory into the `project_location` specified by the use and then makes a new directory using 
                `project_name` and goes into the directory and creates new project based on `selected` infrastructure, makes folder 
                git repository and then makes empty .gitignore file and prints text in the console
                """
                os.system('cd "{}" && mkdir {} && cd {} && dotnet new {} && dotnet build && git init && touch > .gitignore && echo Done bootstrapping project && echo Edit the template .gitignore file in the folder I created!'.format(
                    project_location, project_name, project_name, selected))

                """ Opens created .gitignore and appends `gitignore_template` var contents to the file and then saves the file """
                with open('{}/{}/.gitignore'.format(project_location, project_name), "a") as gitignore_file:
                    gitignore_file.writelines(gitignore_template)

        elif not is_sub_directory:

            op = platform.system()  # Operating system
            # User selected infrastructure type searching the available short names for dotnet infrastructures
            selected = infrastructure_short_names.get(infrastructure)

            if op == "Windows":

                """
                Goes to the `project_location` specified and then creates new dotnet project and makes git repository out of it
                Makes empty .gitignore file and prints text to screen, then opens project folder in Windows Explorer->(Windows only)
                Then writes content to newly created .gitignore file using `gitignore_template` also opens Google Chrome
                """

                default_chrome_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

                os.system('cd "{}" && dotnet new {} && dotnet build && git init && type nul > .gitignore && echo Done bootstrapping project && echo Edit the template .gitignore file in the folder I created! && explorer . && {} && echo Opened Google Chrome application now visit the site on https://localhost:5000, this is where I will stop && dotnet run'.format(
                    project_location, selected, default_chrome_location))
                with open('{}/{}/.gitignore'.format(project_location, project_name), "a") as gitignore_file:
                    gitignore_file.writelines(gitignore_template)

            elif op == "Darwin" or op == "Linux":

                """
                Goes to the `project_location` specified and then creates new dotnet project and makes git repository out of it
                Makes empty .gitignore file and prints text to screen, then writes content of `gitignore_template`
                to the newly created .gitignore file
                """

                finished_text_1 = puts(
                    f"{colored.green('Done bootstrapping project')}")
                finished_text_2 = puts(
                    f"{colored.cyan('Edit the template .gitignore file in the folder I created!')}")

                os.system('cd "{}" && dotnet new {} && dotnet build && git init && touch .gitignore && echo "{}" && echo "{}"'.format(
                    project_location, selected, finished_text_1, finished_text_2))


"""
Edit this file to update and add features to the general `.net` framework preset.
Just be careful of follow the labels and don't break anything.
When coding this file I made use of ---->> code ligatures!
"""

"""
The follow are project TODO:
1. Make options and checkboxes work to customize project creation
2. Automatically open an installed editor ----> IDE ---->> using global settings
3. Make opening ----> Google Chrome work
4. Make code |> really shorter
"""
