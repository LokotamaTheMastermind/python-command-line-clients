def welcome_banner():
    from clint.textui import puts, indent, colored
    from pyfiglet import Figlet

    figlet = Figlet(font='slant')
    header = 'Package Uninstaller'
    puts(colored.red(figlet.renderText(header)))

    with indent(6, quote=' >'):
        puts(colored.cyan(
            'Uninstall any package from the most common package managers out there!'))
