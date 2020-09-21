# -*- coding: utf-8 -*-

from clint.textui import colored, puts
from PyInquirer import prompt, Separator

""" Dotnet tool jumpstart """


def dot_net_jumpstart(framework, is_in_a_sub_folder, project_location, project_name, is_git_repository):

    from utils.scope_vars import extra_questions, infrastructure_short_names

    def using_web_development_application_type(answers):
        return answers['using_web_development_application_type']

    def not_using_web_development_application_type(answers):
        return not answers['using_web_development_application_type']

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
