from clint.textui import colored, puts, indent


""" Function for normal quickstarting of django projects """
""" Django jumpstart function """


def django_jumpstart(framework, folder_location, project_name, sub_folder):
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

    virtualenv = os.path.exists(f"{folder_location}/venv")

    if virtualenv:
        import platform
        import os
        op = platform.system()  # User-based operating system

        if op == "Windows":
            activation = os.system(
                '{}/venv/Scripts/activate'.format(folder_location))
            if activation == 0:
                os.system(
                    '{}/venv/Scripts/activate && pip install django'.format(folder_location))
                """
                This runs an Windows command for changing directory to the `project_location` and then starting activates a virtualenv and then it starts a project based on value specified in `project_name`
                """
                os.system('cd "{}" && {}/venv/Scripts/activate && django-admin startproject {} .'.format(
                    folder_location, folder_location, project_name))
            elif activation == 1:
                puts(
                    f'{colored.red("Activation Error")}: this occured when activating virtualenv!')
        elif op == "Darwin" or op == "Linux":
            """ Step 1 - Validate if `pipenv` is installed then upgrade or install fresh if neccessary """
            try:
                import pipenv
                import os

                os.system('pip3 install --upgrade pipenv')
            except ImportError:
                import os

                os.system('pip3 install pipenv')

            """ Step 2 - Run all neccessary commands for setting up `django project` and `pipenv` """
            activation = os.system(
                'cd "{}" && pipenv install django && pipenv shell'.format(folder_location))

            if activation == 0:
                if sub_folder:
                    os.system('cd "{}" && pipenv shell && django-admin startproject {} {} && cd {} && python3 manage.py migrate && python manage.py createsuperuser --email=admin@{}.com --username=admin && echo "Done making the project and started development server on port 5000" && python3 manage.py runserver 5000'.format(
                        folder_location, project_name, project_name, project_name, project_name))
                elif sub_folder:
                    os.system('cd "{}" && pipenv shell && django-admin startproject {} . && python3 manage.py migrate && python3 manage.py createsuperuser --email=admin@{}.com --username=admin && echo "Started development server on port 5000" && python3 manage.py runserver'.format(folder_location, project_name, project_name))
            elif activation == 1:
                puts(
                    f'{colored.red("Activation Error")}: this occured when activating virtualenv!')
    elif not virtualenv:
        import platform
        import os

        op = platform.system()

        if sub_folder:
            if op == "Windows":
                os.system('cd "{}" && virtualenv {} && {}\\Scripts\\activate && pip install django && django-admin startproject {} {} && cd {} && python manage.py migrate && python manage.py createsuperuser --email=admin@{}.com --username=admin && echo Done making the project and started development server on port 5000 && python manage.py runserver 5000'.format(
                    folder_location, project_name, project_name, project_name, project_name, project_name, project_name))
            elif op == "Darwin" or op == "Linux":
                os.system('cd "{}" pipenv install django && pipenv shell && django-admin startproject {} {} && cd {} && python3 manage.py migrate && python3 manage.py createsuperuser --email=admin@{}.com --username=admin && echo "Done making the project and started development server on port 5000" && python3 manage.py runserver 5000'.format(
                    folder_location, project_name, project_name, project_name, project_name))
        elif not sub_folder:
            if op == "Windows":
                os.system()
