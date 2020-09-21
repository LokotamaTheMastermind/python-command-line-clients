from PyInquirer import Separator

""" Welcome view question set """
questions = [
    {
        # Framework Jumpstarter
        'type': 'list',
        'name': 'framework',
        'message': '* Choose the framework to jumpstart |',
        'choices': [
            {
                'name': '.net'
            },
            {
                'name': 'python'
            },
            {
                'name': 'javascript'
            },
            {
                'name': 'php'
            },
        ],
    },
    {
        # Project name
        'type': 'input',
        'name': 'project_name',
        'message': f'* Name of project (myproject) |',
        'default': 'myproject',
    },
    {
        # Project location
        'type': 'input',
        'name': 'location',
        'message': '* Location of created project |'
    },
    {
        # Project in sub-folder [Y/N]
        'type': 'confirm',
        'name': 'is_sub_folder',
        'message': 'Do you want your project in a sub-folder?',
        'default': False
    },
    {
        # Additional project feature
        'type': 'checkbox',
        'name': 'additional_stuff',
        'message': 'Select more stuff your want for your project',
        'choices': [
            Separator('= General Stuff ='),
            {
                'name': 'Item 1'
            },
            {
                'name': 'Item 2'
            },
            {
                'name': 'Item 3'
            },
        ]
    },
]


""" List of all application frameworks for jumpstarting """
""" Add optional frameworks here! """
framework_presets = [
    '.net',
    'django',
    'flask',
    'c# (console)',
    'c++ (console)',
    'symfony',
    'laravel',
    'reactjs',
    'vuejs',
    'angularjs',
    'backbonejs',
    'aureliajs'
    'python',
]
