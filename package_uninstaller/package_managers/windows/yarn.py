# -*- coding: utf-8 -*-

from clint.textui import puts, colored
from PyInquirer import prompt


""" Define windows package delete function for yarn """


def package_manager_yarn(global_package, containerized_package):
    import os
    import click
    import re

    if global_package and not containerized_package:
        puts(colored.white(
            "The list of available globally packages to uninstall are"))
        print("")
        os.system(
            'cd extra/files/yarn && yarn global list > packages.txt')

        file = open('extra/files/yarn/packages.txt',
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
            os.system('yarn global remove {}'.format(package_name))
            puts(
                f'\n{colored.yellow("Uninstalled package {}".format(package_name))}')
            quit()
        elif not confirmation:
            puts(
                f'\n{colored.green("Thank God you decided not to uninstall the package {}!".format(package_name))}')
            quit()

    elif containerized_package and not global_package:
        puts('\nUsing normal yarn package environments\n')

        more_question = [
            {
                'name': 'folder_location',
                'type': 'input',
                'message': 'Enter full path of folder containing project using yarn |'
            }
        ]

        answer = prompt(more_question)
        folder_path = answer['folder_location']

        if folder_path != "":
            drive_pattern = re.compile('[A-Z]\\:')
            is_a_drive = re.search(drive_pattern, folder_path)
            drive_letter = folder_path.split(':')[0]
            changed_drive = os.chdir(f'{drive_letter}:')
            main_folder = folder_path.split(':')[1]
            correct_folder = os.path.exists(f'{main_folder}/yarn.lock')

            if not correct_folder:
                print("")
                puts(colored.red(
                    'Sorry an error occurred with verifying if folder is an actual yarn project'))
                exit()
            elif correct_folder:
                print("")
                activated = os.system(
                    'cd "{}" && mkdir info && cd info && type nul > packages.txt && yarn list > packages.txt'.format(folder_path))

                with open('{}/info/packages.txt'.format(folder_path)) as package_file:
                    content = package_file.readlines()
                    for line in content:
                        click.echo_via_pager(line)

                if activated == 1:
                    puts(
                        f"{colored.red('Error')}: while listing dependencies in the yarn project")
                    exit()

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
                    activated = os.system(
                        'cd "{}" && yarn remove {}'.format(folder_path, package_name))

                    if activated == 0:
                        puts(
                            f'\n{colored.yellow("Uninstalled package {}".format(package_name))}')
                    elif activated == 1:
                        puts(
                            f"{colored.red('Error')}: while deleting dependencies in the yarn project")
                    quit()
                elif not confirmation:
                    puts(
                        f'\n{colored.green("Thank God you decided not to uninstall the package {}!".format(package_name))}')
                    quit()


"""
If you wanna contribute whats really needed is what is in written as a --> `TODO`
I love folding code
"""
