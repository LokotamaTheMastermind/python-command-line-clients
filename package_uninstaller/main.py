from clint.textui import puts, indent, colored
from pyfiglet import Figlet
from PyInquirer import prompt
from extra import welcome_banner
from extra.global_vars import questions


# Entry point in function
def main():
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
    action(package_manager, is_global, is_local)


def action(package_manager, global_package, containerized_package):

    import os
    import platform
    import click

    op = platform.system()  # Operating system

    if op == "Windows":

        if package_manager == "pip":

            if global_package and not containerized_package:

                puts(colored.white(
                    "The list of available globally packages to uninstall are"))
                print("")
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
                    virtualenv = f'{folder_path}/{virtualenv_name}/'
                    virtualenv.replace('/', '\\')
                    activated = os.system(
                        '"{}\\Scripts\\activate"'.format(virtualenv))

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

        elif package_manager == "yarn":

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

                    correct_folder = os.path.exists(
                        f'{folder_path}/yarn.lock')

                    if not correct_folder:
                        print("")
                        puts(colored.red(
                            'Sorry an error occurred with verifying if folder is an actual yarn project'))
                        exit()
                    elif correct_folder:
                        print("")
                        os.system(
                            'cd "{}" && yarn list'.format(folder_path))

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
                            puts(
                                f'\n{colored.yellow("Uninstalled package {}".format(package_name))}')
                            quit()
                        elif not confirmation:
                            puts(
                                f'\n{colored.green("Thank God you decided not to uninstall the package {}!".format(package_name))}')
                            quit()


if __name__ == "__main__":
    main()


"""
This file doesn't yet support using files in another drive like `D:` or `A:` apart from `C:` drive that
comes default to Windows
"""
