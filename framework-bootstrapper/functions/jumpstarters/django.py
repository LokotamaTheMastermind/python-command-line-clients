from clint.textui import colored, puts, indent


""" Function for normal quickstarting of django projects """
""" Django jumpstart function """


def django_jumpstart(framework, folder_location, project_name):
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
                    folder_location, root_dir, project_name))
            elif activation == 1:
                puts(
                    f'{colored.red("Activation Error")}: this occured when activating virtualenv!')
