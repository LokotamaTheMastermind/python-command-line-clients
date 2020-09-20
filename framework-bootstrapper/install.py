""" Installation of the CLI """

""" Important Modules """
import platform
import os

""" Dynamic operating system """
op = platform.system()

if op == "Windows":
    # os.system('cd %homepath% && mkdir bin && cd bin && mkdir lokotamathemastermind && cd lokotamathemastermind && mkdir framework_bootstrapper && copy "%homepath%/Downloads/framework_bootstrapper/bootstrapper.py" "%homepath%/bin/framework_bootstrapper"')
    os.environ.setdefault('FRAMEWORK_BOOTSTRAPPER', '%homepath%/bin/lokotamathemastermind/framework_bootstrapper/bootstrapper.py')
    os.system('doskey framework-bootstrapper = python %FRAMEWORK_BOOTSTRAPPER%')
