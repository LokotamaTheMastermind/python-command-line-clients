from .global_vars import questions, framework_presets


def welcome_banner():

    from clint.textui import indent, colored, puts
    from pyfiglet import Figlet

    """ Massive banner """
    figlet = Figlet(font='slant')
    header = 'Framework Jumpstarter'
    puts(colored.green(figlet.renderText(header)))

    """ Information banner with indentation! """
    with indent(6, quote=f' {colored.cyan("~!>")} '):
        # Information
        first_line = colored.blue(
            'This is a command line client for jump starting any programming language framework supported')

        # More Information
        second_line = colored.yellow(
            "List of available commands are coming soon!")

        # Quick tip
        third_line = colored.cyan(
            "Quick tip: all fields marked * are important and leaving them will result in an error or wrongly jumpstarted projects!")

        information = """ {} \n {} \n {} """.format(
            first_line, second_line, third_line)
        puts(information)
