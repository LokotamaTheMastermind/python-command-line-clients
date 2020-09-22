# -*- coding: utf-8 -*-

from clint.textui import puts, colored
from PyInquirer import prompt


""" Define windows package delete function for pip """


def package_manager_pip(global_package, containerized_package):
    import click
    import os

    if global_package and not containerized_package:
        # TODO: uninstallation of multiple packages

        puts(colored.white(
            "The list of available globally packages to uninstall are"))
        print("")
        # TODO: change base path for packages.txt in global `pip` listing
        os.system('cd extra/files/pip && pip list > packages.txt')

        file = open('extra/files/pip/packages.txt',
                    'r', encoding='utf-8')

        content = file.readlines()

        for line in content:
            click.echo_via_pager(line.strip())

        extra_questions = [
            {
                'name': 'package_name',
                'type': 'input',
                'message': 'Enter package name for uninstallation |',
                'default': 'foo'
            },
            {
                'name': 'confirmation',
                'type': 'confirm',
                'message': 'Are you sure you wanna delete this package?',
                'default': False,
            }
        ]

        answers = prompt(extra_questions)

        package_name = answers['package_name']
        confirmation = answers['confirmation']

        if confirmation:
            print("")
            os.system('pip uninstall {} -y'.format(package_name))
            puts(
                f'\n{colored.yellow("Uninstalled package {}".format(package_name))}')
            quit()
        elif not confirmation:
            puts(
                f'\n{colored.green("Thank God you decided not to uninstall the package {}!".format(package_name))}')
            quit()

    elif not global_package and containerized_package:
        # TODO: add pagination for the long list of `pip` packages after writing to a file using `clint.echo_via_pager()` function
        # TODO: deletion of multiple `virtualenv` packages

        puts('\nUsing virtualenv package for python virtual environments\n')

        more_question = [
            {
                'name': 'folder_location',
                'type': 'input',
                'message': 'Enter full path of folder containing virtualenv |'
            },
            {
                'name': 'virtualenv_name',
                'type': 'input',
                'message': 'Enter name of virtualenv |',
            }
        ]

        answer = prompt(more_question)
        folder_path = answer['folder_location']
        virtualenv_name = answer['virtualenv_name']

        if not folder_path == "":
            # TODO: change this to work with all paths
            virtualenv = f'{folder_path}/{virtualenv_name}/'
            virtualenv.replace('/', '\\')
            activated = os.system('"{}\\Scripts\\activate"'.format(virtualenv))

            if activated == 1:
                puts(colored.red(
                    'Sorry an error occurred with virtualenv activation'))
                exit()
            elif activated == 0:
                print("")
                activated = os.system(
                    '"{}\\Scripts\\activate" && pip list'.format(virtualenv))

                extra_questions = [
                    {
                        'name': 'package_name',
                        'type': 'input',
                        'message': 'Enter package name for uninstallation |',
                        'default': 'foo'
                    },
                    {
                        'name': 'confirmation',
                        'type': 'confirm',
                        'message': 'Are you sure you wanna delete this package?',
                        'default': False,
                    }
                ]

                answers = prompt(extra_questions)
                package_name = answers['package_name']
                confirmation = answers['confirmation']

                # TODO: add custom error messages for not install pip package
                if confirmation:
                    activated = os.system(
                        '"{}\\Scripts\\activate" && pip uninstall {} -y'.format(virtualenv, package_name))
                    puts(
                        f'\n{colored.yellow("Uninstalled package {}".format(package_name))}')
                    quit()
                elif not confirmation:
                    puts(
                        f'\n{colored.green("Thank God you decided not to uninstall the package {}!".format(package_name))}')
                    quit()


"""
If you wanna contribute whats really needed is what is in written as a --> `TODO`
I love folding code
"""
