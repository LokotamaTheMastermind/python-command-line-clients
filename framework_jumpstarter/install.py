""" Installation of the CLI """

""" Important Modules """

""" Dynamic operating system """
import platform
import os
op = platform.system()

os.environ.setdefault('FRAMEWORK_BOOTSTRAPPER',
                      '%homepath%/bin/lokotamathemastermind/framework_bootstrapper/entry.py')
os.system('doskey jumpstarter = python %FRAMEWORK_BOOTSTRAPPER%')
